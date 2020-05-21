from django.contrib import admin

# from .models import BackGroungImage

# importamos las clases que creamos desde nuestro modelo
from gestion_BBDD.models import Causa, Numeradore 

# Register our models here.
class DatosCausas(admin.ModelAdmin):

    # list_display permite mostrar los distintos campos por separado
    # list_display=("nro_causa", "caratula", "juzgado", "tel_juzgado","resp_PNA")
    list_display=("nro_causa",)
    # permite hacer búsquedas en los campos que se inserten. En este caso es "causa"
    # search_fields=("nro_causa","juzgado")
    search_fields=("nro_causa",)
    #se agregan filtros por causa y juzgado
    # list_filter=("resp_PNA",)



admin.site.register(Causa, DatosCausas)   # permite agregar DatosCausas a Causa
admin.site.register(Numeradore)

# admin.site.register(BackgroundImage)