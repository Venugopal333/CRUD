from django.contrib import admin
from CrudApp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','No','Name','Marks','Address']
admin.site.register(Student,StudentAdmin)

