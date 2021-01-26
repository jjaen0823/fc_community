from django import forms
from django.contrib.auth.hashers import check_password
from .models import Fcuser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label='User Name',
        error_messages={
            'required': 'User Name field is required'
        }
    )
    password = forms.CharField(widget=forms.PasswordInput, label='Password',
        error_messages={
            'required': 'Password field is required'
        })  # PasswordInput: 번호가 가려서 보임

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', 'User does not exist.')
                return 
            
            if not check_password(password, fcuser.password):
                self.add_error('password', 'Your Password is wrong!')
            else:
                self.user_id = fcuser.id