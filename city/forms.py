from django.forms import forms

from city.choices import *


class CViewerForm(forms.Form):
    status = forms.ChoiceField(choices=STATE_CHOICES, label="", initial='', widget=forms.Select(), required=True)
