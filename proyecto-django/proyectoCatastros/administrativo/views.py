from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from administrativo.serializers import UserSerializer, GroupSerializer, \
CasaSerializer, DepartamentoSerializer, PersonaSerializer, BarrioSerializer
# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# Create your views here.
# casas
def index(request):
    """
        Listar los registros del modelo casas
        obtenidos de la base de datos.
    """
    casas = Casa.objects.all()
   
    informacion_template = {'casas': casas, 'numero_casas': len(casas)}
    return render(request, 'index.html', informacion_template)

# departamentos 

# Ver departamentos
def dept(request):
    departamentos = Departamento.objects.all()
   
    informacion_template = {'departamentos': departamentos, 'numero_departamentos': len(departamentos)}
    return render(request, 'dept.html', informacion_template)

# Crear Casa
@login_required(login_url='/entrando/login/')
def crear_casa(request):
    """
    """
    if request.method=='POST':
        formulario = CasaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = CasaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearCasa.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.change_casa', )
def editar_casa(request, id):
    """
    """
    casa = Casa.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasaForm(request.POST, instance=casa)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaForm(instance=casa)
    diccionario = {'formulario': formulario}

    return render(request, 'editarCasa.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.delete_casa', )
def eliminar_casa(request, id):
    """
    """
    casa = Casa.objects.get(pk=id)
    casa.delete()
    return redirect(index)



# Crear Departamento
def crear_departamento(request):
    """
    """
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(dept)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearDepartamento.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.change_departamento', )
def editar_departamento(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(dept)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editarDepartamento.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.delete_departamento', )
def eliminar_departamento(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)


# Ingreso y salida (Logeo)
def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'Registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

# PERSONAS
def personas(request):
    """
        Listar los registros del modelo casas
        obtenidos de la base de datos.
    """
    personas = Persona.objects.all()
   
    informacion_template = {'personas': personas}
    return render(request, 'personas.html', informacion_template)

def eliminar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index)

def crear_persona(request):
    """
    """
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(personas)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearPersona.html', diccionario)

def editar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(personas)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)

#BARRIOS

def barrios(request):
    """
        Listar los registros del modelo casas
        obtenidos de la base de datos.
    """
    barrios = Barrio.objects.all()
   
    informacion_template = {'barrios': barrios}
    return render(request, 'barrios.html', informacion_template)

def eliminar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(barrios)

def crear_barrio(request):
    """
    """
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(barrios)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)

def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(barrios)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)




# USO DE SERIALIZERS
# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class BarrioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]

class CasaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
# class NumeroTelefonicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
