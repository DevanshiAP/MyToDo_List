from django import forms
from .models import Todolist

class Todolistform(forms.ModelForm):
   class Meta:
       model = Todolist
       fields = "__all__"
