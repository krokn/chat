from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    username = forms.CharField(
        label="Логин",
        max_length=150,  # Можно изменить, но лучше оставить 150 символов
        error_messages={
            "required": "Это поле обязательно!",  # Убирает стандартное сообщение
            "max_length": "Максимальная длина — 150 символов.",
            "invalid": "Разрешены только буквы, цифры и символы @/./+/-/_"
        }
    )

    class Meta:
        model = User
        fields = ["username", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")