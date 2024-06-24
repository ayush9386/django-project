from django import forms
from .models import Logger


shifts = (
    ("1" , "Morning"),
    ("2" , "Evening"),
    ("3" , "Night"),
          )
class InputForm(forms.Form):
    first_name = forms.CharField(max_length= 50)
    last_name = forms.CharField(max_length= 50)
    shift = forms.ChoiceField(choices= shifts)
    time_log= forms.TimeField(required=False, help_text= 'enter the exact time')


#using model Form
class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'