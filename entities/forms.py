from django import forms
from .models import Entity


class EntityModelForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = [
            'user',
            'title',
            'content',
            'image'
        ]

    def clean(self):
        content = self.cleaned_data.get('content')
        image = self.cleaned_data.get('image')

        if content == "":
            content = None
        if content is None and image is None:
            raise forms.ValidationError("Content or image is required")
        return super().clean()
