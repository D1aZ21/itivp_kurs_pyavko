from .models import AuthUser,Bookg
from django.forms import ModelForm
from django import forms


class RegisterForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = ["full_name","phone_number", "password","email"]
class BookingForm(ModelForm):
    class Meta:
        model = Bookg
        fields = ['user','device','hall','booking_time', 'hours','price']
        widgets = {
             'booking_time': forms.TimeInput(attrs={
                'type': 'time',  # Поле времени
                'class': 'timepicker',  # Можете добавить класс для стилизации
                'required': 'required'
            }),
            'hours': forms.NumberInput(attrs={
                'min': 1,  # Минимальное значение для числа часов
                'class': 'hours-input',  # Класс для стилизации
                'required': 'required'
            }),
        }