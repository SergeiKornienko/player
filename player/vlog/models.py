from django.db import models
from django.urls import reverse
from django.utils import timezone


class Video(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    file = models.FileField('Видео', upload_to='videos/')
    uploaded = models.DateTimeField('Дата загрузки', default=timezone.now)
    playlist = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
