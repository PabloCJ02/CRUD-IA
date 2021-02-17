from django.db import models

# Create your models here.
class Temario(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=150)

    class Meta: 
        db_table = 'temario'

