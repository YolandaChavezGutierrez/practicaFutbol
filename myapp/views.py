from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Arbitros, Cedulas, Equipos, Estadios, Juegos, Jugadores, Ligas
from .forms import CrearNuevoArbitro,  CrearNuevaCedula, CrearNuevoEquipo, CrearNuevoEstadio, CrearNuevoJuego, CrearNuevoJugador, CrearNuevaLiga, EditarArbitro, EditarCedula, EditarEquipo, EditarEstadio, EditarJuego, EditarJugador, EditarLiga

# Create your views here.
def index(request):
    return render(request, 'index.html')

def juegos(request):
    juegos = Juegos.objects.all()
    return render(request, 'juegos.html',{
        'juegos': juegos })

def ligas(request):
    ligas = Ligas.objects.all()
    return render(request, 'ligas.html',{
        'ligas': ligas })

def cedulas(request):
    cedulas = Cedulas.objects.all()
    return render(request, 'cedulas.html',{
        'cedulas': cedulas })

def equipos(request):
    equipos = Equipos.objects.all()
    return render(request, 'equipos.html',{
        'equipos': equipos })

def arbitros(request):
    arbitros = Arbitros.objects.all()
    return render(request, 'arbitros.html',{
        'arbitros': arbitros })

def estadios(request):
    estadios = Estadios.objects.all()
    return render(request, 'estadios.html',{
        'estadios': estadios })

def jugadores(request):
    jugadores = Jugadores.objects.all()
    return render(request, 'jugadores.html',{
        'jugadores': jugadores })

def crear_arbitro(request):
    if request.method == 'GET':
        return render(request, 'crear_arbitro.html',{
            'form': CrearNuevoArbitro() })
    else:
        Arbitros.objects.create(imagen=request.FILES['imagen'],
        nombre=request.POST['nombre'], 
        liga_id=request.POST['liga'])
        return redirect('/arbitros/')

def crear_cedula(request):
    if request.method == 'GET':
        return render(request, 'crear_cedula.html',{
            'form': CrearNuevaCedula() })
    else:
        Cedulas.objects.create(fecha=request.POST['fecha'], 
        horaInicio=request.POST['horaInicio'],
        horaFin=request.POST['horaFin'],
        resultado=request.POST['resultado'],
        estado=request.POST['estado'],
        juego_id=request.POST['juego'])
        return redirect('/cedulas/')

def crear_equipo(request):
    if request.method == 'GET':
        return render(request, 'crear_equipo.html',{
            'form': CrearNuevoEquipo() })
    else:
        Equipos.objects.create(imagen=request.FILES['imagen'],
        nombre=request.POST['nombre'], 
        entrenador=request.POST['entrenador'],
        juegosGanados=request.POST['juegosGanados'],
        juegosPerdidos=request.POST['juegosPerdidos'],
        liga_id=request.POST['liga'])
        return redirect('/equipos/')

def crear_estadio(request):
    if request.method == 'GET':
        return render(request, 'crear_estadio.html',{
            'form': CrearNuevoEstadio() })
    else:
        Estadios.objects.create(imagen=request.FILES['imagen'],
        nombre=request.POST['nombre'], 
        liga_id=request.POST['liga'])
        return redirect('/estadios/')
    
def crear_juego(request):
    if request.method == 'GET':
        return render(request, 'crear_juego.html',{
            'form': CrearNuevoJuego() })
    else:
        Juegos.objects.create(fecha=request.POST['fecha'], 
        estadio_id=request.POST['estadio'],
        liga_id=request.POST['liga'],
        contrincante_id=request.POST['equipo']),
        return redirect('/juegos/')

def crear_jugador(request):
    if request.method == 'GET':
        return render(request, 'crear_jugador.html',{
            'form': CrearNuevoJugador() })
    else:
        Jugadores.objects.create(imagen=request.FILES['imagen'],
        nombre=request.POST['nombre'],
        numeroPlayera=request.POST['numeroPlayera'],
        posicion=request.POST['posicion'],
        equipo_id=request.POST['equipo'])
        return redirect('/jugadores/')

def crear_liga(request):
    if request.method == 'GET':
        return render(request, 'crear_liga.html',{
            'form': CrearNuevaLiga() })
    else:
        Ligas.objects.create(imagen=request.FILES['imagen'],
        nombre=request.POST['nombre'],
        poblacion=request.POST['poblacion'],
        estado=request.POST['estado'])
        return redirect('/ligas/')
    
def eliminar_arbitro(request, arbitro_id):
    arbitro = Arbitros.objects.get(id=arbitro_id)
    if request.method == 'POST':
        arbitro.delete()
        return redirect('/arbitros/')
    return render(request, 'arbitros.html', {'arbitro': arbitro})

def editar_arbitro(request, arbitro_id):
    arbitro = get_object_or_404(Arbitros, id=arbitro_id)
    data ={
        'form': EditarArbitro(instance=arbitro) }
    if request.method == 'POST':
        formulario = EditarArbitro(data=request.POST, instance=arbitro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/arbitros/')
    return render(request, 'editar_arbitro.html', data)

def eliminar_cedula(request, cedula_id):
    cedula = Cedulas.objects.get(id=cedula_id)
    if request.method == 'POST':
        cedula.delete()
        return redirect('/cedulas/')
    return render(request, 'cedulas.html', {'cedula': cedula})

def editar_cedula(request, cedula_id):
    cedula = get_object_or_404(Cedulas, id=cedula_id)
    data ={
        'form': EditarCedula(instance=cedula) }
    if request.method == 'POST':
        formulario = EditarCedula(data=request.POST, instance=cedula, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/cedulas/')
    return render(request, 'editar_cedula.html', data)

def eliminar_equipo(request, equipo_id):
    equipo = Equipos.objects.get(id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('/equipos/')
    return render(request, 'equipos.html', {'equipo': equipo})

def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipos, id=equipo_id)
    data ={
        'form': EditarEquipo(instance=equipo) }
    if request.method == 'POST':
        formulario = EditarEquipo(data=request.POST, instance=equipo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/equipos/')
    return render(request, 'editar_equipo.html', data)

def eliminar_estadio(request, estadio_id):
    estadio = Estadios.objects.get(id=estadio_id)
    if request.method == 'POST':
        estadio.delete()
        return redirect('/estadios/')
    return render(request, 'estadios.html', {'estadio': estadio})

def editar_estadio(request, estadio_id):
    estadio = get_object_or_404(Estadios, id=estadio_id)
    data ={
        'form': EditarEstadio(instance=estadio) }
    if request.method == 'POST':
        formulario = EditarEstadio(data=request.POST, instance=estadio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/estadios/')
    return render(request, 'editar_estadio.html', data)

def eliminar_juego(request, juego_id):
    juego = Juegos.objects.get(id=juego_id)
    if request.method == 'POST':
        juego.delete()
        return redirect('/juegos/')
    return render(request, 'juegos.html', {'juego': juego})

def editar_juego(request, juego_id):
    juego = get_object_or_404(Juegos, id=juego_id)
    data ={
        'form': EditarJuego(instance=juego) }
    if request.method == 'POST':
        formulario = EditarJuego(data=request.POST, instance=juego, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/juegos/')
    return render(request, 'editar_juego.html', data)

def eliminar_jugador(request, jugador_id):
    jugador = Jugadores.objects.get(id=jugador_id)
    if request.method == 'POST':
        jugador.delete()
        return redirect('/jugadores/')
    return render(request, 'jugadores.html', {'jugador': jugador})

def editar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugadores, id=jugador_id)
    data ={
        'form': EditarJugador(instance=jugador) }
    if request.method == 'POST':
        formulario = EditarJugador(data=request.POST, instance=jugador, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/jugadores/')
    return render(request, 'editar_jugador.html', data)

def eliminar_liga(request, liga_id):
    liga = Ligas.objects.get(id=liga_id)
    if request.method == 'POST':
        liga.delete()
        return redirect('/ligas/')
    return render(request, 'ligas.html', {'liga': liga})

def editar_liga(request, liga_id):
    liga = get_object_or_404(Ligas, id=liga_id)
    data ={
        'form': EditarLiga(instance=liga) }
    if request.method == 'POST':
        formulario = EditarLiga(data=request.POST, instance=liga, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/ligas/')
    return render(request, 'editar_liga.html', data)