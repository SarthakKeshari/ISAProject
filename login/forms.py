from django import forms
from .models import LoginDetails

class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder':'Username'
        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control',
            'placeholder':'Password',
        }   
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
    	model = LoginDetails
    	fields = ('username', 'password')
class LoginDetailsForm(MyModelForm):
	form_class = MyModelForm
