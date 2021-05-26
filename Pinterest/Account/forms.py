from django import forms
from django.contrib.auth.forms import UserCreationForm

#__init__
class AccountUpdateForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].disabled=True
