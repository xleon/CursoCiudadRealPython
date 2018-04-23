from django.db import models

class School(models.Model):
    name = models.CharField('Nombre', max_length=30)
    address = models.CharField('Dirección', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Escuela'

class Student(models.Model):
    name = models.CharField('Nombre', max_length=30)
    age = models.IntegerField('Edad')
    school = models.ForeignKey(
        School, 
        verbose_name='Escuela', 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estudiante'
