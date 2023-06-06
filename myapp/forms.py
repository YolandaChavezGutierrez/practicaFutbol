from django import forms
from .models import Ligas, Juegos, Estadios, Equipos, Arbitros, Cedulas, Jugadores

class EditarArbitro(forms.ModelForm):
    class Meta:
        model= Arbitros
        fields = ['imagen','nombre', 'liga']
class CrearNuevoArbitro(forms.Form):
        imagen = forms.ImageField(label="Foto")
        nombre = forms.CharField(label="Nombre del arbitro", max_length=100)
        liga = forms.ModelChoiceField(label="Liga del arbitro", queryset=Ligas.objects.all())

class EditarCedula(forms.ModelForm):
    class Meta:
        model= Cedulas
        fields = ['fecha','horaInicio', 'horaFin', 'resultado', 'estado', 'juego']
class CrearNuevaCedula(forms.Form):
    fecha = forms.DateField(label="Fecha", initial="2023-05-20") 
    horaInicio = forms.TimeField(label="Hora de inicio", initial="10:00")
    horaFin = forms.TimeField(label="Hora de fin", initial="11:00")
    resultado = forms.CharField(label="Resultado", max_length=100)
    estado = forms.CharField(label="Estado", max_length=100)
    juego = forms.ModelChoiceField(label="Juego", queryset=Juegos.objects.all())

class EditarEquipo(forms.ModelForm):
    class Meta:
        model= Equipos
        fields = ['imagen','nombre', 'entrenador', 'juegosGanados', 'juegosPerdidos', 'liga']
class CrearNuevoEquipo(forms.Form):
    imagen = forms.ImageField(label="Foto")
    nombre = forms.CharField(label="Nombre del equipo", max_length=100)
    entrenador = forms.CharField(label="Nombre del entrenador", max_length=100)
    juegosGanados = forms.IntegerField(label="Juegos ganados")
    juegosPerdidos = forms.IntegerField(label="Juegos perdidos")
    liga = forms.ModelChoiceField(label="Liga del equipo", queryset=Ligas.objects.all())

class EditarEstadio(forms.ModelForm):
    class Meta:
        model= Estadios
        fields = ['imagen','nombre', 'liga']
class CrearNuevoEstadio(forms.Form):
    imagen = forms.ImageField(label="Foto")
    nombre = forms.CharField(label="Nombre del estadio", max_length=100)
    liga = forms.ModelChoiceField(label="Liga del estadio", queryset=Ligas.objects.all())

class EditarJuego(forms.ModelForm):
    class Meta:
        model= Juegos
        fields = ['fecha','estadio', 'liga', 'contrincante']
class CrearNuevoJuego(forms.Form):
    fecha = forms.DateTimeField(label="Fecha", initial="2023-05-20 09:00") 
    estadio = forms.ModelChoiceField(label="Estadio", queryset=Estadios.objects.all())
    liga = forms.ModelChoiceField(label="Liga", queryset=Ligas.objects.all())
    equipo = forms.ModelChoiceField(label="Contrincante", queryset=Equipos.objects.all())

class EditarJugador(forms.ModelForm):
    class Meta:
        model= Jugadores
        fields = ['imagen','nombre', 'numeroPlayera', 'posicion', 'equipo']
class CrearNuevoJugador(forms.Form):
    imagen = forms.ImageField(label="Foto")
    nombre = forms.CharField(label="Nombre del jugador", max_length=100)
    numeroPlayera = forms.CharField(label="Numero de playera", max_length=100)
    posicion = forms.CharField(label="Posicion", max_length=100)
    equipo = forms.ModelChoiceField(label="Equipo", queryset=Equipos.objects.all())

class EditarLiga(forms.ModelForm):
    class Meta:
        model= Ligas
        fields = ['imagen','nombre', 'poblacion', 'estado']
class CrearNuevaLiga(forms.Form):
    imagen = forms.ImageField(label="Foto")
    nombre = forms.CharField(label="Nombre de la liga", max_length=100)
    poblacion = forms.CharField(label="Poblacion", max_length=100)
    estado = forms.CharField(label="Estado", max_length=100)