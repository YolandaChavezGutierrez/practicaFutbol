from django.contrib import admin
from .models import Ligas, Estadios, Juegos, Equipos, Arbitros, Jugadores, Cedulas

# Register your models here.
admin.site.register(Ligas) 
admin.site.register(Estadios) 
admin.site.register(Juegos)
admin.site.register(Equipos)
admin.site.register(Arbitros)   
admin.site.register(Jugadores)
admin.site.register(Cedulas)

  