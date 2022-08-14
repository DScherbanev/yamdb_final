from django.core.mail import send_mail


def send_email(token, email):
    send_mail(
        'Регистрация на сайте YAMDb',
        f'Ваш адрес был указан для регистрации на сайте YAMDb.\n'
        f'Для продолжения регистрации используйте код: {token}',
        'pavel.a.agapov@yandex.ru',
        [f'{email}'],
        fail_silently=False,
    )
