from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, AuthenticationForm as DjangoAuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import *
from .utils import send_email_for_verify

User = get_user_model()

class AddWorkspace(forms.ModelForm):
    class Meta:
        model = Workspaces
        fields =('name_workspace', 'describe_workspace',  )
        # fields ='__all__'
        widgets={
            'name_workspace': forms.TextInput(attrs={'class': 'form - input'}),
            'describe_workspace': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        }
    def clean_name_workspace(self):
        name_workspace = self.cleaned_data['name_workspace']
        if len(name_workspace)>50:
            raise ValidationError('Длина превышает 50 символов')
        return name_workspace



class AddColumn(forms.ModelForm):
    class Meta:
        model = Columns
        fields = ('name_column', 'describe_column', 'id_workspace')
        # fields ='__all__'
        widgets={
            'name_column': forms.TextInput(attrs={'class': 'form-input'}),
            'describe_column': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        }


class AddTask(forms.ModelForm):
    class Meta:
        model = Cards
        fields ='__all__'
        widgets={
            'name_card': forms.TextInput(attrs={'class': 'form-input'}),
            'describe_card': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        }

class AddAccess(forms.ModelForm):
    class Meta:
        model = Members
        fields ='__all__'

# class RegisterUserForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields =('username', 'email', 'password1', 'password2')
#         widgets={
#             'username': forms.TextInput(attrs={'class': 'form-input'}),
#             'email': forms.EmailInput(attrs={'class': 'form-input'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
#         }

class AuthenticationForm(DjangoAuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )

            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Почта не подтверждена. Мы снова отправили вам ссылку. Проверьте свою почту',
                    code='invalid_login',
                )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget= forms.EmailInput(attrs={'autocomplete': 'email'})

    )

    class Meta(DjangoUserCreationForm.Meta):
        model=User
        fields =('username', 'email', 'password1', 'password2')