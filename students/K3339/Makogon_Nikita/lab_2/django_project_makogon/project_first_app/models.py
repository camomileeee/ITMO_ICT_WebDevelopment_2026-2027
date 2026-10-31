from django.db import models

from django.db import models

class CarOwner(models.Model):
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Car(models.Model):
    state_number = models.CharField(max_length=15, verbose_name="Гос. номер")
    brand = models.CharField(max_length=20, verbose_name="Марка")
    model_name = models.CharField(max_length=20, verbose_name="Модель")
    color = models.CharField(max_length=30, null=True, blank=True, verbose_name="Цвет")

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.state_number})"

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, verbose_name="Владелец")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")

    def __str__(self):
        return f"{self.owner} — {self.car} (с {self.start_date})"

class DriverLicense(models.Model):
    LICENSE_TYPES = (
        ('A', 'Категория A'),
        ('B', 'Категория B'),
        ('C', 'Категория C'),
        ('D', 'Категория D'),
    )
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, verbose_name="Владелец")
    license_number = models.CharField(max_length=10, verbose_name="Номер удостоверения")
    type = models.CharField(max_length=10, choices=LICENSE_TYPES, verbose_name="Тип")
    issue_date = models.DateField(verbose_name="Дата выдачи")

    def __str__(self):
        return f"{self.license_number} ({self.type}) — {self.owner}"