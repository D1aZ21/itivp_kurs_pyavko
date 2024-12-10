// Убедитесь, что код выполняется после загрузки DOM
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM полностью загружен');

    document.getElementById('forgotPasswordLink').addEventListener('click', function(e) {
        e.preventDefault();
        alert('Функция восстановления пароля пока не доступна!');
    });

    document.getElementById('registerLink').addEventListener('click', function(e) {
        e.preventDefault();
        console.log('Нажали на ссылку "Регистрация"');
        // Показываем ссылку на возврат к авторизации
        let backToAuthLink = document.createElement('a');
        backToAuthLink.href = '#';
        backToAuthLink.textContent = 'Назад к авторизации';
        backToAuthLink.id = 'backToAuthLink';
        document.querySelector('.auth-links').appendChild(backToAuthLink);

        // Убираем старые ссылки
        document.getElementById('registerLink').style.display = 'none';
    });

    // Возврат к авторизации
    document.addEventListener('click', function(e) {
        if (e.target && e.target.id == 'backToAuthLink') {
            e.preventDefault();
            console.log('Возвращаемся к форме авторизации');
            document.querySelector('label[for="password"]').style.display = 'inline-block';
            document.getElementById('formTitle').textContent = 'Авторизация';
            document.getElementById('phone').placeholder = 'Введите номер телефона';
            document.getElementById('password').style.display = 'block'; // Показать поле пароля
            document.querySelector('button').textContent = 'Войти';

            // Убираем добавленные поля и ссылки
            document.getElementById('backToAuthLink').remove();
            document.querySelector('#registerLink').style.display = 'inline-block'; // Показываем ссылку на регистрацию
            document.querySelector('#forgotPasswordLink').style.display = 'inline-block'; // Показываем ссылку на восстановление пароля
            document.getElementById('fullName')?.remove(); // Убираем поле ФИО (если оно есть)
            document.getElementById('email')?.remove(); // Убираем поле email (если оно есть)
            document.querySelector('label[for="fullName"]')?.remove(); // Удаляем лейбл для ФИО
            document.querySelector('label[for="email"]')?.remove(); // Удаляем лейбл для email
        }
    });
});
