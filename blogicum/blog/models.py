from django.db import models

from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        null=False,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        null=False,
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры,'
            ' дефис и подчёркивание.'
        )
    )
    is_published = models.BooleanField(
        default=True,
        null=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        verbose_name='Добавлено'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        null=False,
        verbose_name='Название места'
    )
    is_published = models.BooleanField(
        default=True,
        null=False,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        verbose_name='Добавлено'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        null=False,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        null=False,
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        null=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        blank=False,
        verbose_name='Категория'
    )
    is_published = models.BooleanField(
        default=True,
        null=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        verbose_name='Добавлено'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
