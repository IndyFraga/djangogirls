from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Alumno(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    nombre = models.TextField()
    apellido_p = models.TextField()
    domicilio = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Empresa(models.Model):
    author = models.ForeignKey('auth.User')
    nombre = models.TextField()
    rfc = models.TextField()
    domicilio = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    author = models.ForeignKey('auth.User')
    nombre = models.TextField()
    horarios = models.TextField()
    dias_clase = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    fecha_inicio = models.DateTimeField(
        blank=True, null=True)
    fecha_fin = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre