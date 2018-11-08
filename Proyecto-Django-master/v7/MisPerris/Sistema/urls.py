from django.conf.urls import url 
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^gestionUsuario/$',views.gestionarUsuarios,name="gestionUsuario"),
    url(r'^gestionMascota/$',views.gestionarMascota,name="gestionMascota"),
    url(r'^ListaPerros/$',views.ListaPerros,name="ListaPerros"),
    url(r'^registro/$',views.registro,name="registro"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^olvidoPass/$',views.olvidoPass,name="olvidoPass"),
    url(r'^restablecerPass/$',views.restablecerPass,name="restablecerPass"),
    ]