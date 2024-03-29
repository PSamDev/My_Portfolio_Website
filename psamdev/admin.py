from django.contrib import admin
from . models import Message


# Register your models here.
class AdminMessage(admin.ModelAdmin):
    list_display = ("name", "email", "message")

admin.site.register(Message, AdminMessage)
