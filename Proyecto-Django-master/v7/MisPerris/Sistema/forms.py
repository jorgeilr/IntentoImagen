from django import forms
perfiles=(
    ('Administrador','Administrador'),
    ('Invitado','Invitado'),
    ('Usuario','Usuario'),
)
resultadosPosibles = (
        ('Seleccione', 'Seleccione'),
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
        )
regiones =(
        ('Seleccione', 'Seleccione'),
        ('Metropolitana', 'Metropolitana'),
        ('I Tarapaca', 'I Tarapaca'),
        ('II Antofagasta', 'II Antofagasta'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
)
ciudades =(
        ('Seleccione', 'Seleccione'),
        ('Santiago', 'Santiago'),
        ('Valparaiso', 'Valparaiso'),
        ('Valparaiso', 'Valparaiso'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),
        ('Santiago', 'Concepcion'),

)
tiposHogar =(
        ('Seleccione', 'Seleccione'),
        ('Casa con patio grande', 'Casa con patio grande'),
        ('Casa con patio pequeño', 'Casa con patio pequeño'),
        ('Departamento', 'Departamento'),

)
class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    rut=forms.CharField(widget=forms.TextInput(),label="Rut")
    perfil=forms.ChoiceField(choices=perfiles)
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre Completo")
    #fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1900,2018)),label="Fecha de Nacimiento")
    #telefono=forms.IntegerField(widget=forms.NumberInput(),label="telefono de contacto")
    #region=forms.MultipleChoiceField(choices=regiones,widget=forms.Select(),label="Region :")
    #ciudad=forms.MultipleChoiceField(choices=ciudades,widget=forms.Select(),label="Ciudad :")
    #tipoHogar=forms.MultipleChoiceField(choices=tiposHogar,widget=forms.Select(),label="Tipo de hogar :")
class RegistrarseForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    rut=forms.CharField(widget=forms.TextInput(),label="Rut")
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre Completo")
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
class AgregarMascota(forms.Form):        
        #fichaMascota=forms.IntegerField(widget=forms.TextInput(),label="Ficha de Mascota :")
        fotoMascota=forms.ImageField(label="Fotografia")
        nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre Mascota :")
        razaMascota=forms.CharField(widget=forms.TextInput(),label="Raza Mascota :")  
        descripcion=forms.CharField(widget=forms.Textarea(),label="Descripcion :")
        estadoMascota=forms.ChoiceField(choices=resultadosPosibles)
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario:")

class RestablecerForm(forms.Form):
    contra1=forms.CharField(widget=forms.PasswordInput(),label="Nueva Contraseña:")
    contra2=forms.CharField(widget=forms.PasswordInput(),label="Ingresar Nueva Contraseña:")

