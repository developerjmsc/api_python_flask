# Importa las bibliotecas necesarias de Flask y decouple.
from flask import Blueprint, jsonify
from decouple import config

# Crea un Blueprint para las rutas del sistema. Un Blueprint es una forma de organizar las rutas en una aplicación Flask.
main = Blueprint("System_blueprint", __name__)


# Define una ruta para "/" que devuelve información sobre el estado del sistema.
@main.route("/")
def system_info():
    """
    Retorna información sobre el estado del sistema.

    Retorna:
    tuple: Una tupla que contiene un diccionario JSON con la información del estado del sistema y el código de estado HTTP.
           El diccionario contiene los siguientes campos:
           - nameSystem (str): Nombre del sistema.
           - version (str): Versión del sistema.
           - developer (str): Nombre del desarrollador del sistema.
           - email (str): Correo electrónico del desarrollador del sistema.
    """
    try:
        # Retorna un objeto JSON con la información del estado del sistema y un código de estado HTTP 200.
        # La información del estado del sistema se obtiene de las variables de entorno usando la biblioteca decouple.
        return (
            jsonify(
                {
                    "nameSystem": config("SYSTEM_NAME"),
                    "version": config("SYSTEM_VERSION"),
                    "developer": config("DEVELOPER_NAME"),
                    "email": config("DEVELOPER_EMAIL"),
                }
            ),
            200,  # Código de estado HTTP OK
        )
    except Exception as ex:
        # Si ocurre algún error, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 500.
        return (
            jsonify({"message": str(ex)}),
            500,
        )  # Código de estado HTTP 500 en caso de error
