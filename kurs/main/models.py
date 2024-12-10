from django.db import models


class TariffCategory(models.Model):
    name = models.CharField(max_length=100)  # Название категории, например "ПК" или "PlayStation"

    def __str__(self):
        return self.name

class Tariff(models.Model):
    category = models.ForeignKey(TariffCategory, on_delete=models.CASCADE, related_name="tariffs")
    description = models.CharField(max_length=100)  # Описание, например "1 час", "VIP ночь"
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Цена

    def __str__(self):
        return f"{self.category.name} - {self.description} ({self.price} BYN)"


class AuthUser(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    password = models.CharField(max_length=255, verbose_name="Пароль")
    role = models.CharField(
        max_length=10,
        default='user',
        verbose_name="Роль"
    )

    def __str__(self):
        return self.phone_number

class Bookg(models.Model):
    user = models.ForeignKey(AuthUser, related_name='bookings', on_delete=models.CASCADE)
    device = models.CharField(max_length=255, verbose_name="Устройство")
    hall = models.CharField(max_length=255, verbose_name="Зал")
    booking_time = models.TimeField()
    hours = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.user.phone_number} for {self.device} in {self.hall} at {self.booking_time} for {self.hours} hours"