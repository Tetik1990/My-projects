from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False, upload_to='images/%Y/%m/%d/')
    description = models.TextField()

    def __str__(self):
        return self.description