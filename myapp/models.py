from django.db import models

# Create your models here.

class Ligas(models.Model):
    imagen = models.ImageField(null=True, upload_to="uploads/")
    nombre = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Equipos(models.Model):
    imagen = models.ImageField(null=True, upload_to="uploads/")
    nombre = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)
    liga = models.ForeignKey(Ligas, on_delete=models.CASCADE)
    juegosGanados = models.IntegerField()
    juegosPerdidos = models.IntegerField()

    def __str__(self):
        return self.nombre 

class Estadios(models.Model):
    imagen = models.ImageField(null=True, upload_to="uploads/")
    nombre = models.CharField(max_length=50)
    liga = models.ForeignKey(Ligas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

class Juegos(models.Model):
    fecha = models.DateTimeField(null=True)
    liga = models.ForeignKey(Ligas, on_delete=models.CASCADE) 
    contrincante = models.ForeignKey(Equipos, on_delete=models.CASCADE)   
    estadio = models.ForeignKey(Estadios, on_delete=models.CASCADE) 

class Arbitros(models.Model):
    imagen = models.ImageField(null=True, upload_to="uploads/")
    nombre = models.CharField(max_length=100)
    liga = models.ForeignKey(Ligas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

class Jugadores(models.Model):
    imagen = models.ImageField(null=True, upload_to="uploads/")
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    numeroPlayera = models.IntegerField()
    posicion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cedulas(models.Model):
    fecha = models.DateField(null=True)
    horaInicio = models.TimeField(null=True)
    horaFin = models.TimeField(null=True)
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
