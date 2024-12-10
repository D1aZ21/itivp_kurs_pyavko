from .models import TariffCategory, AuthUser, Bookg
from django.shortcuts import render, redirect
from .forms import RegisterForm, BookingForm
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)



def index(request):
    categories = TariffCategory.objects.prefetch_related('tariffs').all()
    return render(request,'main/index.html', {'categories': categories})
def auth(request):
    error = ''
    if request.method == 'POST':
        action = request.POST.get('action')  # Узнаем, что выбрал пользователь (логин или регистрация)
        if action == 'login':
            # Авторизация
            phone_number = request.POST.get('phone')
            password = request.POST.get('password')

            try:
                user = AuthUser.objects.get(phone_number=phone_number, password=password)
                if user.role == 'user':
                    request.session['user_id'] = user.id
                    return redirect('user')  # Переадресация на главную страницу
                else :
                    return redirect('manager')  # Переадресация на главную страницу
            except AuthUser.DoesNotExist:
                messages.error(request, 'Неверный номер телефона или пароль.')

        elif action == 'register':
             form = RegisterForm(request.POST)
             if form.is_valid():
                form.save()
                messages.success(request, 'Регистрация прошла успешно.')
                return redirect('auth')
             else:
                error = 'Форма была неверной'

    form = RegisterForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/auth.html', context)
def user(request):
    error = ''
    user_id = request.session.get('user_id')
    if user_id:
        user = AuthUser.objects.get(id=user_id)
    else:
        # Если пользователя нет в сессии, можно перенаправить на страницу авторизации
        return redirect('auth')
    categories = TariffCategory.objects.prefetch_related('tariffs').all()

    if request.method == 'POST':
        initial_data = {
            'device': request.POST.get('device'),
            'hall': request.POST.get('hall'),
            'booking_time': request.POST.get('booking_time'),
            'hours': request.POST.get('hours'),
            'price': request.POST.get('price'),
            'user': user
        }

        form = BookingForm(initial_data)  # Передаем только данные POST

        print(f"Время бронирования: {request.POST}")

        if form.is_valid():
            form.save()
            print(f"Бронирование прошло успешно.")
            messages.success(request, 'Бронирование прошло успешно.')
            return redirect('user')
        else:
            # Выводим ошибки валидации
            print(form.errors)  # Это покажет, какие поля не прошли валидацию
            error = 'Форма была неверной'
            messages.error(request, error)
            return redirect('user')  # Redirect to the user's profile or another page

    bookings = user.bookings.all()  # Получаем все бронирования текущего пользователя
    form = BookingForm()
    context = {
        'form': form,
        'error': error,
        'categories': categories,
        'bookings': bookings,
        'user': user  # Передаем информацию о пользователе в контекст
    }
    return render(request, 'main/user.html', context)
def admin(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'register':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Регистрация прошла успешно.')
                return redirect('manager')
            else:
                error = 'Форма была неверной'
                messages.success(request,error)
        elif action == 'booking':
            device = request.POST.get('device')  # Получаем устройство
            hall = request.POST.get('hall')  # Получаем зал
            booking_time = request.POST.get('booking_time')  # Получаем время
            hours = request.POST.get('hours')  # Получаем число часов
            user_phone = request.POST.get('userPhoneBooking')  # Получаем номер телефона

            # Теперь вы можете использовать эти значения для создания бронирования или другой логики
            print("Устройство:", device)
            print("Зал:", hall)
            print("Время:", booking_time)
            print("Часы:", hours)
            print("Телефон пользователя:", user_phone)
            user = AuthUser.objects.get(phone_number=request.POST.get('userPhoneBooking'))
            initial_data = {
                'device': request.POST.get('device'),
                'hall': request.POST.get('hall'),
                'booking_time': request.POST.get('booking_time'),
                'hours': request.POST.get('hours'),
                'price': hours*5,
                'user':  user
            }

            form = BookingForm(initial_data)  # Передаем только данные POST
            if form.is_valid():
                form.save()
                print(f"Бронирование прошло успешно.")
                messages.success(request, 'Бронирование прошло успешно.')
                return redirect('manager')
            else:
                # Выводим ошибки валидации
                print(form.errors)  # Это покажет, какие поля не прошли валидацию
                error = 'Форма была неверной'
                messages.error(request, error)
                return redirect('manager')  # Redirect to the user's profile or another page
        elif action == 'ban':
            blockUserPhone = request.POST.get('blockUserPhone')
            print("blockUserPhone:", blockUserPhone)
            user = AuthUser.objects.get(phone_number=request.POST.get('blockUserPhone'))
            user.delete()
    all_users = AuthUser.objects.all()
    form = BookingForm()
    form2 = RegisterForm()
    context = {
        'form': form,
        'form2': form2,
        'all_users': all_users
    }
    return render(request, 'main/admin.html', context)