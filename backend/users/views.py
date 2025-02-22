from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "users/login.html", {"form": form})


def chats_view(request):
    chats = [
        {'id': 1, 'name': 'Рабочий чат'},
        {'id': 2, 'name': 'Друзья'},
        {'id': 3, 'name': 'Семья'},
    ]

    selected_chat = {
        'id': 1,
        'name': 'Рабочий чат',
    } if request.GET.get('chat_id') else None

    messages = [
        {'sender': 'Алексей', 'text': 'Привет! Как дела?'},
        {'sender': 'Ты', 'text': 'Привет! Все хорошо, спасибо!'},
    ] if selected_chat else []

    return render(request, 'users/chats.html', {
        'chats': chats,
        'selected_chat': selected_chat,
        'messages': messages,
    })


def logout_view(request):
    logout(request)
    return redirect("login")
