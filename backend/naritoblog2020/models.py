from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    slug = models.SlugField('スラッグ', unique=True)
    text = models.TextField('本文')
    description = models.TextField('概要', blank=True)
    image = models.ImageField('サムネイル')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
