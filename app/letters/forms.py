from django import forms

from .models import Letter, LetterComment


class LetterCreateForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = "__all__"
        widgets = {
            "date_on_doc": forms.TextInput(attrs={"type": "date"}),
            "date_received": forms.TextInput(attrs={"type": "date"}),
            "subject": forms.Textarea(attrs={"rows": 3}),
            # "copied_to": forms.Select(attrs={"multiple": "multiple"}),
        }


class LetterCommentCreateForm(forms.ModelForm):
    class Meta:
        model = LetterComment
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 3}),
        }
