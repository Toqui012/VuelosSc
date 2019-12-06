from django.shortcuts import render
from .models import cotizacion
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Import para el formulario de registro y el login más logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect



# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    
    """
    #Renderiza la Plantilla HTML index.html con los datos en la variable contexto

    return render(
        request,
        'index.html',
        
    )

def carrete(request):
    """
    Función vista para la página inicio del sitio.
    
    """
    #Renderiza la Plantilla HTML index.html con los datos en la variable contexto

    return render(
        request,
        'carrete.html',
        
    )

def register(request):
    status = ''
    if request.method == 'POST':
        user = User()
        try:
            user = User.objects.create_user(username = request.POST.get('nombre'),
            password = request.POST.get('pass'),
            first_name = request.POST.get('telefono'),
            last_name = request.POST.get('apellido'),
            email = request.POST.get('email'))
        except:
            print(status)
            status = 'ERROR'
            return render(request,'register.html',{'status': status})
        user.save()
        status = 'OK'
        print(status)
        # list = User.objects.all() query de prueba para ver si se estaban registrando
        print(list)
    return render(
        request,'register.html',{'status':status}
    )

def login_view(request):
    status = ''
    if request.method == 'POST':
        username = request.POST.get('nombre')
        password = request.POST.get('pass')
        print(username)
        print(password)
        user = authenticate(request, username = username , password = password)
        if user:
            login(request, user)
            status = 'OK'
            print(status)
            return HttpResponseRedirect(reverse('index'))
        else:
            status = 'ERROR'
            print(status)
            messages.error(request,'ERROR AL INICIAR SESIÓN')
    variables = {'status':status}
    return render(request,'login.html',variables)

@login_required(login_url = 'login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')

class ListacotizacionVista(generic.ListView):
    model    =    cotizacion
    context_object_name ='cotizacion_list' # your own name    for    the    list as    a template    variable
    template_name =    'destinos/cotizacion_list.html'


class cotizacionCreate(CreateView):
    model = cotizacion
    fields= '__all__'


class cotizacionUpdate(UpdateView):
    model = cotizacion
    fields = ['nombre','rut','email','mensaje']


class cotizacionDelete(DeleteView):
    model = cotizacion
    success_url= reverse_lazy('cotizacion')

class cotizacionDetailView(generic.DeleteView):
    model = cotizacion

