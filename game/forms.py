from django import forms

from . import models


class MapImageForm(forms.ModelForm):
    class Meta:
        model = models.MapImage
        fields = ['image']
