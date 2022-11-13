from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        print(self.cleaned_data)
        username = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)

        if not username or not password:
            raise forms.ValidationError("Please enter both fields")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("invalid credentials")

        return super(LoginForm, self).clean()
