from django.apps import AppConfig


# creamos una clase con el nombre de la app que creamos
class GestionBbddConfig(AppConfig):
    name = 'gestion_BBDD'

    

# incluimos esta clase en settings.py, dentro de la lista de INSTALLED_APPS