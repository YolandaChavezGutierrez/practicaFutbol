from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('juegos/', views.juegos),
    path('ligas/', views.ligas),
    path('cedulas/', views.cedulas),
    path('equipos/', views.equipos),
    path('arbitros/', views.arbitros),
    path('estadios/', views.estadios),
    path('jugadores/', views.jugadores),
    path('crear_arbitro/', views.crear_arbitro),
    path('crear_cedula/', views.crear_cedula),
    path('crear_equipo/', views.crear_equipo),
    path('crear_estadio/', views.crear_estadio),
    path('crear_juego/', views.crear_juego),
    path('crear_jugador/', views.crear_jugador),
    path('crear_liga/', views.crear_liga),
    path('arbitros/<int:arbitro_id>/', views.eliminar_arbitro, name='eliminar_arbitro'),
    path('editar_arbitro/<int:arbitro_id>/', views.editar_arbitro,name='editar_arbitro'),
    path('cedulas/<int:cedula_id>/', views.eliminar_cedula, name='eliminar_cedula'),
    path('editar_cedula/<int:cedula_id>/', views.editar_cedula,name='editar_cedula'),
    path('equipos/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('editar_equipo/<int:equipo_id>/', views.editar_equipo,name='editar_equipo'),
    path('estadios/<int:estadio_id>/', views.eliminar_estadio, name='eliminar_estadio'),
    path('editar_estadio/<int:estadio_id>/', views.editar_estadio,name='editar_estadio'),
    path('juegos/<int:juego_id>/', views.eliminar_juego, name='eliminar_juego'),
    path('editar_juego/<int:juego_id>/', views.editar_juego,name='editar_juego'),
    path('jugadores/<int:jugador_id>/', views.eliminar_jugador, name='eliminar_jugador'),
    path('editar_jugador/<int:jugador_id>/', views.editar_jugador,name='editar_jugador'),
    path('ligas/<int:liga_id>/', views.eliminar_liga, name='eliminar_liga'),
    path('editar_liga/<int:liga_id>/', views.editar_liga,name='editar_liga'),
]