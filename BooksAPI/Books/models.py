from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Author(models.Model):
    author_name = models.CharField(max_length=500)
    about_author = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    education = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    occupation = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(unique=True)
    author_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.author_name

def create_slug(instance, new_slug=None):
    slug = slugify(instance.author_name)
    if new_slug is not None:
        slug = new_slug
    qs = Author.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Author)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


#pre_save.connect(pre_save_post_receiver, sender=Author)


class Book(models.Model):
    book_name = models.CharField(max_length=500)
    about_book = models.TextField()
    genre = models.CharField(max_length=500, blank=True, null=True)
    No_of_pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=500, blank=True, null=True)
    book_image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.SET('N/A'), blank=True, null=True)

    def __str__(self):
        return self.book_name
