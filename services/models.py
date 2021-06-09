from django.db import models
from django.urls import reverse


# from django.shortcuts import redirect


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Тип услуги')
    content = models.TextField(verbose_name='Описание услуги', blank=True)
    price = models.IntegerField(verbose_name='Стоимость')
    duration = models.CharField(blank=True, max_length=100, verbose_name='продолжительность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления услуги')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    amount = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('services:show_works_by_category', kwargs={'category_id': self.pk})


class Additional(models.Model):
    add_name = models.CharField(max_length=150, verbose_name='Наименование услуги')
    content = models.TextField(blank=True, verbose_name='Описание услуги')
    price = models.IntegerField(verbose_name='Стоимость')
    duration = models.CharField(blank=True, max_length=100, verbose_name='продолжительность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления услуги')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.add_name

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'
        ordering = []


class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    telephone_number = models.CharField(max_length=150, verbose_name='Номер телефона клиента')
    activity = models.CharField(max_length=150, verbose_name='Род деятельности', blank=True)
    birthday = models.DateField(verbose_name='День рождения', blank=True, default='10.12.2000')
    number_of_visits = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photo/clients/%Y/%m/%d', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = []

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)


class Visit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Клиент', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Услуга', blank=True)
    additional = models.ManyToManyField(Additional, blank=True, verbose_name='Доп. услуги')
    work_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата визита', blank=True)
    price = models.IntegerField(default='250', verbose_name='Стоимость', blank=True)
    duration = models.DurationField(default='03:00:00', help_text='часы:минуты:секунды',
                                    verbose_name='Длительность процедуры', blank=True)
    content = models.TextField(blank=True, verbose_name='Описание процедуры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo_before = models.ImageField(upload_to='photo/visits/before/%Y/%m/%d', blank=True, verbose_name='Фото до')
    photo_after = models.ImageField(upload_to='photo/visits/after/%Y/%m/%d', blank=True, verbose_name='Фото после')

    class Meta:
        verbose_name = 'Визит'
        verbose_name_plural = 'Визиты'
        ordering = ['-work_date']

    def __str__(self):
        return self.category.category_name

    def get_absolute_url(self):
        return reverse('services:show_work', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Visit, on_delete=models.CASCADE, verbose_name='Комментарий')
    name = models.CharField(max_length=150, default='Noone')
    email = models.EmailField(default='email@gmail.com')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    content = models.TextField(verbose_name='Содерджание комментария')
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Cleaning(models.Model):
    step_name = models.CharField(max_length=150, verbose_name='Номер этапа')
    content = models.TextField(blank=True, verbose_name='Описание процедуры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Этап очистки'
        verbose_name_plural = 'Страница "Стерилизация"'
        ordering = []

    def __str__(self):
        return self.step_name


class VisitAsk(models.Model):
    telephone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    client_name = models.CharField(max_length=100, verbose_name='Как Вас зовут', blank=True)
    comment = models.TextField(verbose_name='Комментарий', default='123')
    additional = models.ManyToManyField(Additional, verbose_name='Доп услуги')

    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Тип маникюра')

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('services:show_visit', kwargs={'visit_pk': self.pk})
