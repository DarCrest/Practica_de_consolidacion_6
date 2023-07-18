from django.shortcuts import render, HttpResponseRedirect
from .forms import Agregar_Vehiculo, UserRegisterForm

# from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Vehiculo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


# Create your views here.


def index(request):
    return render(request, "vehiculo/index.html")


@login_required(login_url='/login/')
@permission_required(perm='vehiculo.add_vehiculomodel', raise_exception=True)
def vehiculo_add(request):
    if request.method == 'POST':
        form = Agregar_Vehiculo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha agregado correctamente')
            return HttpResponseRedirect("/vehiculo/add/")
    else:
        form = Agregar_Vehiculo()
        context = {'form': form}
        return render(request, 'vehiculo/add.html', context)


@login_required(login_url='/login/')
@permission_required(perm='vehiculo.visualizar_catalogo', raise_exception=True)
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'vehiculo/list.html', context)


def login_(request):
    if request.user.is_authenticated:
        messages.info(request, 'Sesión Iniciada')
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Bienvenido {username}.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Usuario o contraseña incorrecta')
                return HttpResponseRedirect('/login')
        else:
            messages.error(request, 'Usuario o contraseña incorrecta')
            return HttpResponseRedirect('/login')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'vehiculo/login.html', context)


def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'Sesión Iniciada')
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo = Permission.objects.get(
                codename='visualizar_catalogo', content_type=content_type)
            user = form.save()
            user.user_permissions.add(visualizar_catalogo)

            login(request, user)
            messages.success(request, 'Se ha creado el ususario')
            return HttpResponseRedirect('/')
        else:
            messages.error(
                request, 'Registro invalido. Datos no son correctos')
        return HttpResponseRedirect('/register/')
    form = UserRegisterForm
    context = {'form': form}
    return render(request, 'vehiculo/register.html', context)


@login_required(login_url='/login/')
def logout_(request):
    logout(request)
    messages.info(request, 'Se ha cerrado sesión correctamente.')
    return HttpResponseRedirect('/')
