from django.db import models


# Creating the models here.

# first we create a class 'Causas', where we create the field we're working with 
# this class will manage information about court cause
class Causa(models.Model):

    
    estado = [
    ('curso', 'En curso'),
    ('elev', 'Elevada'),
    ('tram', 'En espera'),
    ]


    
    nro_causa = models.CharField(max_length=50, verbose_name= "Número de causa")
         
    expediente = models.CharField(max_length=50, verbose_name= "Expediente")
    caratula = models.CharField(max_length=50, verbose_name= "Carátula de causa")

    estado_causa = models.CharField(max_length=10, choices=estado, default='En espera',verbose_name= "Estado de causa")      # probar si fuciona

    fecha = models.DateField(verbose_name="Fecha de Entrada")                                              # fecha de entrada de la causa
       
    fecha_elev2 = models.CharField(max_length=15, verbose_name="Fecha de elevación (DD/MM/AA)",blank=True, null=True)                                                # fecha de elevación de la causa
    juzgado = models.CharField(max_length=50, verbose_name= "Juzgado interviniente")                                         # name of the judge
    resp_juzgado = models.CharField(max_length=50, verbose_name= "Responsable de juzgado")
    tel_juzgado = models.CharField(max_length=12, verbose_name= "Teléfono de juzgado")
    secretaria = models.CharField(max_length=50, verbose_name= "Número de secretaría")
    resp_secretaria = models.CharField(max_length=50, verbose_name= "Responsable de secretaría")
    resp_PNA = models.CharField(max_length=50, verbose_name= "Personal de PNA asignado")
    observ2 = models.TextField(verbose_name= "Observaciones", max_length=400, default='')
    

    def __str__(self):

        return(self.nro_causa)

# here we create a class to manage people information
class Persona(models.Model):

    persona = models.CharField(max_length=50, verbose_name="Personal que lleva a cargo el trámite")         # name of the person who loads up the document  
    direc = models.CharField(max_length=50, verbose_name="Dirección del personal")           # name of the direction which the person belongs to

    def __str__(self):

        return(self.persona)


