from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='Модель телефона')
    price = models.CharField(verbose_name='Цена')
    image = models.URLField(verbose_name='URL ссылка на изображение')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(default=True,verbose_name='Поддержка LTE')
    slug = models.SlugField(unique=True, verbose_name='URL_slug')
    
