from django.contrib import admin

# Register your models here.
from .models import Post, Alumno, Empresa, Materia

admin.site.register(Post)
admin.site.register(Alumno)
admin.site.register(Empresa)
admin.site.register(Materia)