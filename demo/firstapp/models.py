from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=32)

class Item(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Category,0)

    def __str__(self):
        return self.name