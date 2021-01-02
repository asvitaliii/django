from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from .models import Verse
from .forms import VerseForm


def index(request):
    return render(request, 'StartPage/index.html')


def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    elif request.method == "POST":
        login = request.POST.get('login_field')
        email = request.POST.get('email_field')
        pass1 = request.POST.get('password_field')
        pass2 = request.POST.get('password_confirmation_field')

        data = {'login': login, 'email': email, 'pass1': pass1, 'pass2': pass2}

        if pass1 != pass2:
            report = "Пароли не совпадают!"
        elif '' in data.values():
            report = "Все поля должны быть заполнены!"
        elif len(pass1) < 8:
            report = "Слишком короткий пароль!"
        else:
            user = User.objects.create_user(login, email, pass1)
            user.save()
            if user:
                return render(request, "result.html", context={'message': f'Пользователь {login} успешно зарегистрирован!'})

        report = "Неизвестная ошибка"
        data['report'] = report

        return render(request, 'register.html', context=data)


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        data = {}
        name = request.POST.get('login_field')
        password = request.POST.get('password_field')
        user = authenticate(request, username=name, password=password)
        if user is None:
            data['report'] = "Неверный логин или пароль"
            return render(request, 'login.html', context=data)
        else:
            login(request, user)
            return render(request, "result.html", context={'message': f'Вы авторизованы как {name}'})


def logout_user(request):
    logout(request)
    return redirect('/')


def ajax_reg(request) -> JsonResponse:
    response = dict()
    login_val = request.GET.get('login_field')
    try:
        User.objects.get(username=login_val)
        response['message_login'] = 'Логин занят!'
    except User.DoesNotExist:
        response['message_login'] = 'ОК!'
    return JsonResponse(response)


def ajax_log(request) -> JsonResponse:
    try:
        User.objects.get(username=request.GET.get('login_field'))
        return JsonResponse({'res': 'OK'})
    except User.DoesNotExist:
        return JsonResponse({'res': ''})


def verse_list(request):
    return render(request, 'verse_list.html', context={'verses': Verse.objects.all()})


def verse_add(request):
    if request.method == "GET":
        return render(request, 'verse_add.html', context={'verse_form': VerseForm()})
    elif request.method == "POST":
        VerseForm(request.POST).save()
        return redirect('verse_list')


def verse_detail(request, id: int):
    return render(request, 'verse_detail.html', context={'verse': Verse.objects.get(id=id)})

