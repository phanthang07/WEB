from django import forms

class PasswordForm(forms.Form):
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)
