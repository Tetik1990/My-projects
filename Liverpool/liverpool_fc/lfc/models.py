from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = models.CharField(max_length=100, verbose_name="Автор")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория", related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['id']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.PROTECT, )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:  # класс для изменения название самой таблички
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Player(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    country = models.CharField(max_length=100, verbose_name="Страна")
    position = models.CharField(max_length=100, verbose_name="Позиция")
    content = models.TextField(blank=True, verbose_name="Биография")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('player', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        ordering = ['-position']
