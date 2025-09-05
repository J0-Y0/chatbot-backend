from django.contrib import admin
from .models import *

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass
# Register your models here.
