from django.contrib import admin
from .models import TextileOrderFile, TextileOrder


admin.site.register(TextileOrder)
admin.site.register(TextileOrderFile)

