from django.contrib import admin

# Register your models here.
from .models import Student, University, GradProgram, Application, Subject, Major, Minor, Requirements
admin.site.register(Student)
admin.site.register(University)
admin.site.register(GradProgram)
admin.site.register(Application)
admin.site.register(Subject)
admin.site.register(Major)
admin.site.register(Minor)
admin.site.register(Requirements)