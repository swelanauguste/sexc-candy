from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = "__all__"
        widgets = {
            "received": forms.TextInput(attrs={"type": "date"}),
            "expires": forms.TextInput(attrs={"type": "date"}),
        }
