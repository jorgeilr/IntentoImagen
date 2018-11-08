from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import AgregarUsuario,Login,AgregarMascota,RegistrarseForm,RecuperacionForm,RestablecerForm
from .models import Usuario,Mascota
from django.template import loader
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def salir(request):
    logout(request)
    return redirect('/')

#
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"titulo",
    }
    return HttpResponse(plantilla.render(contexto,request)) 

@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    usuarios=Usuario.objects.all()
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(username=data.get("username"),email=data.get("correo"),password=data.get("password"))
        usuario=Usuario(user=regDB,rut=data.get("rut"),perfil=data.get("perfil"),nombre=data.get("nombre"),)
        tipo=data.get("perfil")
        if tipo=="Administrador":
            regDB.is_staff=True
        else:
            regDB.is_staff=False
        regDB.save()
        usuario.save()
   
    form=AgregarUsuario()
    return render(request,"gestionUsuario.html",{'actual':actual,'form':form,'usuarios':usuarios,})
@login_required(login_url='login')
def gestionarMascota(request):
    form = AgregarMascota(request.POST,request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Mascota(fichaMascota=data.get("fichaMascota"),fotoMascota=data.get("fotoMascota"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcion=data.get("descripcion"),estadoMascota=data.get("estadoMascota"),)     
        regDB.save() 
    form = AgregarMascota()
    mascotas=Mascota.objects.all()
    titulo="Gestion Mascotas"
    return render(request,"gestionMascota.html",{'mascotas':mascotas,'form':form,'titulo':titulo,})
def ListaPerros(request):
    mascotas=Mascota.objects.all()
    return render(request,"ListaPerros.html",{'mascotas':mascotas,})
def registro(request):
    form=RegistrarseForm(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       #regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(username=data.get("username"),email=data.get("correo"),password=data.get("password"))
        usuario=Usuario(user=regDB,rut=data.get("rut"),nombre=data.get("nombre"),)
        #regDB.save()
        usuario.save()
    form=RegistrarseForm()
    return render(request,"registro.html",{'form':form,})

def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('/index/')
        
    return render(request,"login.html",{'form':form,})

def olvidoPass(request):
    form=RecuperacionForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=User.objects.get(username=data.get("username"))
        send_mail(
                'ASUNTO',
                'MENSAJE',
                'CORREO',
                [user.email],
                html_message = 'Pulse <a href="http://localhost:8000/restablecePass?user='+user.username+'">aquí</a> para restablecer su contraseña.',
            )
    return render(request,"olvidoPass.html",{'form':form,})

def restablecerPass(request):
    form=RestablecerForm(request.POST or None)
    if form.is_valid():
        try:
            username=request.GET["user"]
        except Exception as e:
            username= None
        if username is not None:
            if form.is_valid():
                data=form.cleaned_data
                if data.get("contra1") == data.get("contra2"):
                    contra=make_password(data.get("contra2"))
                    User.objects.filter(username=username).update(password=contra)
            return render(request,"restablecePass.html",{'form':form, 'username':username,})
        else:
            return redirect('/login/')
