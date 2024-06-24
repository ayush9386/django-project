from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import user_detail
class get_user_detail(forms.ModelForm):
    class Meta:
        model = user_detail
        fields = '__all__'

class display(forms.Form):
    name = forms.CharField(max_length=50)

class edit(display):
    no_of_people = forms.IntegerField()
    def __init__(self , *args, **kwargs):
        super(display , self).__init__(*args,**kwargs)


class delete_data(display):
    def __init__(self , *args, **kwargs):
        super(display, self).__init__(*args , **kwargs)
