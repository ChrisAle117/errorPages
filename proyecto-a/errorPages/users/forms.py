from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    
    password1= forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': True,
                'pattern': '(?=.*[!#$%&?])(?=.*\d).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, un número y un símbolo (!, #, $, %, & o ?).',
                'minlength': 8
            }
        )
    )
    password2= forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar contraseña',
                'required': True,
                'pattern': '(?=.*[!#$%&?])(?=.*\d).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, un número y un símbolo (!, #, $, %, & o ?).',
                'minlength': 8
            }
        )
    )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Por favor, ingrese un correo electrónico de la UTEZ.',
                    'maxlength': 254,
                    'minlength': 8
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required': True,
                    'pattern': '[A-Za-z]+',
                    'title': 'El nombre no debe de contener numeros.',
                    'maxlength': 100,
                    'minlength': 20
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'required': True,
                    'pattern': '[A-Za-z]+',
                    'title': 'El nombre no debe de contener numeros.',
                    'maxlength': 100,
                    'minlength': 20
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de control',
                    'required': True,
                    'pattern': '^\d{5}TN\d{3}$',
                    'title': 'El número de control debe ser una matrícula de la utez.',
                    'minlength': 6,
                    'maxlength': 10,
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                    'min': 18,
                    'max': 100,
                    'title': 'La edad debe estar entre 18 y 100 años.'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'required': True,
                    'pattern': '[0-9]{10}',
                    'title': 'El teléfono debe tener 10 dígitos.'
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$', email):
            raise forms.ValidationError("El correo electrónico debe ser del dominio @utez.edu.mx")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres")
        if not re.search(r'[!#$%&?]', password):
            raise forms.ValidationError("La contraseña debe contener al menos un símbolo (!, #, $, %, & o ?)")
        if not re.search(r'\d', password):
            raise forms.ValidationError("La contraseña debe contener al menos un número")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if len(control_number) != 10:
            raise forms.ValidationError("La matrícula debe tener 10 caracteres")
        return control_number

class CustomUserLoginForm(AuthenticationForm):
    pass



