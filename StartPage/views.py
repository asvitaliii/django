from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from .models import Verse, Author
from .forms import VerseForm, AuthorForm


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
    verse = Verse.objects.get(id=id)
    return render(request, 'verse_detail.html', context={'verse': verse})


def verse_del(request, id: int):
    Verse.objects.get(id=id).delete()
    return redirect('verse_list')


def verse_update(request, id: int):
    data = {}
    verse = Verse.objects.get(id=id)
    data['verse'] = verse
    if request.method == "GET":
        verse_form = VerseForm(instance=verse)
        data['verse_form'] = verse_form
        return render(request, 'verse_update.html', context=data)
    elif request.method == "POST":
        verse_form = VerseForm(request.POST)
        if verse_form.is_valid():
            verse.name = verse_form.cleaned_data['name']
            verse.text = verse_form.cleaned_data['text']
            verse.author = verse_form.cleaned_data['author']
            verse.save()
    return redirect(f'/{id}/verse_detail')


def author_list(request):
    return render(request, 'author_list.html', context={'authors': Author.objects.all()})


def author_add(request):
    if request.method == "GET":
        return render(request, 'author_add.html', context={'author_form': AuthorForm()})
    elif request.method == "POST":
        AuthorForm(request.POST).save()
        return redirect('author_list')


def author_detail(request, id: int):
    return render(request, 'author_detail.html', context={'author': Author.objects.get(id=id), 'verses': Verse.objects.filter(author__id=id)})


def author_del(request, id: int):
    Author.objects.get(id=id).delete()
    return redirect('author_list')


def author_update(request, id: int):
    data = {}
    author = Author.objects.get(id=id)
    data['author'] = author
    if request.method == "GET":
        author_form = AuthorForm(instance=author)
        data['author_form'] = author_form
        return render(request, 'author_update.html', context=data)
    elif request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author.name = author_form.cleaned_data['name']
            author.about = author_form.cleaned_data['about']
            author.save()
    return redirect(f'/{id}/author_detail')
