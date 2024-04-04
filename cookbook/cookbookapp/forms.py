from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100)  # Название
    description = forms.CharField(widget=forms.Textarea)  # Описание
    steps = forms.CharField(widget=forms.Textarea)  # Шаги приготовления
    cook_time = forms.DurationField()  # Время приготовления
    image = forms.ImageField()  # Изображение
    # author = forms.ForeignKey(User, on_delete=models.CASCADE)  # Автор

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def confirm_login_allowed(self, user):
        if user.is_staff and not user.is_superuser:
            raise ValidationError(
                "This account is not allowed here.",
                code='not_allowed',
            )