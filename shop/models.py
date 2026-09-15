from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    old_price = models.IntegerField(blank=True, null=True, verbose_name="Старая цена")
    image = models.ImageField(upload_to='products/', verbose_name="Фото")
    flag = models.ImageField(upload_to='flags/', blank=True, null=True, verbose_name="Флаг")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    article = models.CharField(max_length=100, blank=True, default="", verbose_name="Артикул")
    description = models.TextField(blank=True, default="", verbose_name="Описание")
    sizes = models.CharField(max_length=200, blank=True, default="", verbose_name="Размеры")
    colors = models.CharField(max_length=200, blank=True, default="", verbose_name="Цвета")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    color = models.CharField(max_length=255, blank=True, default="", verbose_name="Цвет")
    year = models.CharField(max_length=50, blank=True, default="", verbose_name="Год")
    wheel_size = models.CharField(max_length=50, blank=True, default="", verbose_name="Диаметр колеса")
    frame_material = models.CharField(max_length=100, blank=True, default="", verbose_name="Материал рамы")
    size = models.CharField(max_length=50, blank=True, default="", verbose_name="Размер")
    country = models.CharField(max_length=100, blank=True, default="", verbose_name="Страна")
    manufacturer = models.CharField(max_length=100, blank=True, default="", verbose_name="Производитель")
    tires = models.CharField(max_length=500, blank=True, default="", verbose_name="Покрышки")
    frame = models.CharField(max_length=500, blank=True, default="", verbose_name="Рама")
    seatpost = models.CharField(max_length=500, blank=True, default="", verbose_name="Подседельный штырь")
    saddle = models.CharField(max_length=500, blank=True, default="", verbose_name="Седло")
    fork = models.CharField(max_length=500, blank=True, default="", verbose_name="Вилка")
    stem = models.CharField(max_length=500, blank=True, default="", verbose_name="Вынос")
    wheels = models.CharField(max_length=500, blank=True, default="", verbose_name="Колеса")
    handlebar = models.CharField(max_length=500, blank=True, default="", verbose_name="Руль")
    brake_type = models.CharField(max_length=100, blank=True, default="", verbose_name="Тип тормозов")
    brake_system = models.CharField(max_length=500, blank=True, default="", verbose_name="Тормозная система")
    shifters = models.CharField(max_length=255, blank=True, default="", verbose_name="Манетки")
    crankset = models.CharField(max_length=500, blank=True, default="", verbose_name="Система шатунов")
    rear_derailleur = models.CharField(max_length=255, blank=True, default="", verbose_name="Задний переключатель")
    chain = models.CharField(max_length=255, blank=True, default="", verbose_name="Цепь")
    speeds = models.CharField(max_length=50, blank=True, default="", verbose_name="Количество скоростей")
    warranty = models.CharField(max_length=50, blank=True, default="", verbose_name="Гарантия")

    def __str__(self):
        return self.title
    
    
    
class WinterBike(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    image = models.ImageField(upload_to='winter_bikes/', verbose_name="Фото")
    flag = models.ImageField(upload_to='flags/', blank=True, null=True, verbose_name="Флаг")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return self.title
    
    
class Equipment(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to='equipment/', verbose_name="Фото")
    price = models.IntegerField(verbose_name="Цена")
    old_price = models.IntegerField(blank=True, null=True, verbose_name="Старая цена")
    is_sold = models.BooleanField(default=True, verbose_name="Продан")

    def __str__(self):
        return self.title
    
class Review(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    tag = models.CharField(max_length=50, default="#обзор", verbose_name="Тег")
    image = models.ImageField(upload_to='reviews/', verbose_name="Фото")
    link = models.URLField(default="#", blank=True, null=True, verbose_name="Ссылка")

    def __str__(self):
        return self.title
    
    
# Create your models here.