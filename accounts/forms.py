from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, User


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


PERMISSIONS_CHOICE = [
    (Permission.objects.get(name='can_view_account').id, 'Accounts'),
    (Permission.objects.get(name='can_view_hr').id, 'HR'),
    (Permission.objects.get(name='can_view_sales').id, 'Sales'),
    (Permission.objects.get(name='can_view_purchase').id, 'Purchase'),
    (Permission.objects.get(name='can_view_reports').id, 'Reports'),

]


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    permissions = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PERMISSIONS_CHOICE,
    )

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email', None)
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        raise forms.ValidationError('This email address is already in use.')
