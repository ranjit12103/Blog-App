from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(_("category name"),max_length=50,unique=True)
    category_image = models.ImageField(_("Category Image"), upload_to='categories/', null=True, blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

STATUS_CHOISE = (
    ("Drafts", "Drafts"),
    ("Published", "Published")
)

class Blog(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    category = models.ForeignKey(Category, verbose_name=_("Categoty"), on_delete=models.CASCADE) 
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    featured_image = models.ImageField(_("Featured Image"), upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(_("Short Description"), max_length=500)
    blog_body = models.TextField(_("Blog Body"), max_length=2000)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOISE, default="Draft")
    is_featured = models.BooleanField(_("Featured or not"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    def __str__(self):
        return self.title













