from django.contrib import admin
from student_profile.models import Student


# Register your models here.

class StudentAdminModel(admin.ModelAdmin):
    pass


admin.site.register(Student)
