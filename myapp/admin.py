from django.contrib import admin
from .models import Student
# Register your models here.
class showstd(admin.ModelAdmin):
    list_display = ["roll","name","email","address","phone"]
admin.site.register(Student,showstd)