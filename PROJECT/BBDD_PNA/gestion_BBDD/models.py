from django.db import models


# Creating the models here.

# first we create a class 'Causas', where we create the field we're working with 
# this class will manage information about court cause
class Causa(models.Model):

    # definición de los posibles estados de las causas
    estado = [('curso', 'En curso'),('elev', 'Elevada'),('tram', 'En espera'),]


    # img = models.ImageField(upload_to='background-image')
    
    # número de causa que se ingresa
    nro_causa = models.CharField(max_length=50, verbose_name= "Número de causa")
    # expediente correspondiente
    expediente = models.CharField(max_length=50, verbose_name= "Expediente")
    # carátula asociada 
    caratula = models.CharField(max_length=50, verbose_name= "Carátula de causa")
    # estado de causa. Se debe elegir entre las opciones dadas
    estado_causa = models.CharField(max_length=10, choices=estado, default='En espera',verbose_name= "Estado de causa")      
    # se debe elegir la fecha de entrada
    fecha = models.DateTimeField(verbose_name="Fecha de Entrada")                                              # fecha de entrada de la causa
    # se debe ingresar a mano la fecha de salida o elevación 
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

# En esta clase creamos la información contenida en el numerador
class Numeradore(models.Model):

    # definición de las opciones del tipo de documento
    tipo_documento = [('oficio', 'Oficio'), ('memorandum', 'Memorándum'), ('acta', 'Acta'), ('vista', 'Vista'), ('dispo', 'Disposición'),
    ('recibo', 'Recibo'),('acta_tar', 'Acta de tarea'),]
    # definición de la clasificación de seguridad
    clasific_seguridad = [('public', 'Público'), ('confi', 'Confidencial'), ('reser', 'Reservado'), ('secret', 'Secreto'),]

    # tipo de documento
    tipo_doc = models.CharField(max_length=20, choices=tipo_documento, default='Oficio',verbose_name= "Tipo de documento")
    #clasificación de seguridad
    clasif_seg = models.CharField(max_length=20, choices=clasific_seguridad, default='Público',verbose_name= "Clasificación de seguridad")
    # número de oficio
    num_oficio = models.IntegerField(verbose_name="Número de oficio")
    # fecha en la que se genera el documento
    fecha_doc = models.DateField(verbose_name="Fecha")
    # campo de texto para agregar alguna referencia al oficio generado
    referencia = models.CharField(max_length=100, verbose_name="Referencia")

    def __str__(self):

        return(self.tipo_documento)


