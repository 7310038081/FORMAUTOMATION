from django import forms

class GoogleFormInput(forms.Form):
    name = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=10)
    address = forms.CharField(max_length=255)
    pin_code = forms.CharField(max_length=6)
    dob = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    captcha_code = forms.CharField(max_length=20)
