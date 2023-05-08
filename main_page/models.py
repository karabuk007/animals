from django.db import models
from django.urls import reverse


class Cats(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    description = models.TextField(blank=True, verbose_name='описание')
    homecountry = models.CharField(max_length=255, verbose_name='страна')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото')
    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_id': self.pk})
    class Meta:
        verbose_name = 'Коты'
        verbose_name_plural = 'Коты'


class Dogs(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    description = models.TextField(blank=True, verbose_name='описание')
    homecountry = models.CharField(max_length=255, verbose_name='страна')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото')
    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_id': self.pk})
    class Meta:
        verbose_name = 'Собаки'
        verbose_name_plural = 'Собаки'

class Classmates(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    description = models.TextField(blank=True, verbose_name='описание')
    homecountry = models.CharField(max_length=255, verbose_name='страна')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото')
    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_id': self.pk})
    class Meta:
        verbose_name = 'Одноклассники'
        verbose_name_plural = 'Одноклассники'

class MainPage(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    description = models.TextField(blank=True, verbose_name='описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото')
    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_id': self.pk})
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'