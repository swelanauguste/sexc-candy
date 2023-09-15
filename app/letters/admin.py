from django.contrib import admin

from .models import Action, Correspondence, Letter, LetterComment

admin.site.register(Action)
admin.site.register(Correspondence)
admin.site.register(Letter)
admin.site.register(LetterComment)
