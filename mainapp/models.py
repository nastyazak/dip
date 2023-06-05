from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользователи"""
    patronymic = models.CharField('Отчество', max_length=50, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=50)
    e_mail = models.EmailField('Адрес электронной почты', max_length=150)
    number = models.CharField('Номер телефона', max_length=11)

    def __str__(self):
        return str(self.username)


class Category(models.Model):
    """Категории работ"""
    name_category = models.CharField(max_length=100)
    category_view = models.CharField(max_length=100, default="checkbox")

    def __str__(self):
        return str(self.name_category)


class TypeWork(models.Model):
    """Виды работ"""
    name_work = models.CharField(max_length=100)
    name_work_estimate = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hours = models.IntegerField(default=1)
    cost = models.IntegerField(default=1000)

    def __str__(self):
        return self.name_work_estimate

