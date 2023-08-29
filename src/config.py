# Importa la biblioteca decouple para manejar la configuración de la aplicación
from decouple import config


# Define una clase Config que contiene la configuración común a todos los entornos.
class Config:
    # Usa la función config de decouple para extraer el valor de la variable de entorno SECRET_KEY.
    # Este es un valor clave que se utiliza para la seguridad en Flask.
    SECRET_KEY = config("SECRET_KEY")


# Define una clase DevelopmentConfig que hereda de Config y representa la configuración específica del entorno de desarrollo.
class DevelopmentConfig(Config):
    # En el entorno de desarrollo, se habilita el modo de depuración para facilitar la solución de problemas.
    DEBUG = True


# Define un diccionario que mapea los nombres de los entornos a sus respectivas clases de configuración.
# Esto permite seleccionar fácilmente la configuración correcta en función del entorno actual.
config = {"development": DevelopmentConfig}
