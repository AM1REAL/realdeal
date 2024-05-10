from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, default='Иван')
    father_name = models.CharField(max_length=50, default='Иванович', blank=True)
    surname = models.CharField(max_length=50, default='Иванов')
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)

class Cords(models.Model):
    latitude = models.FloatField(unique=True)
    longitude = models.FloatField(unique=True)
    height = models.FloatField(unique=True)

class Level(models.Model):
    LEVEL_CHOICES = [
        ('winter', 'Зима'),
        ('spring', 'Весна'),
        ('summer', 'Лето'),
        ('autumn', 'Осень'),
    ]
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

class Image(models.Model):
    title = models.CharField(max_length=35, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/')

class ObjectP(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('pending', 'Рассматривается'),
        ('accepted', 'Принят'),
        ('rejected', 'Отказан'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cords = models.ForeignKey(Cords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    beauty_title = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    other_title = models.TextField(blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
