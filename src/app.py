# Importa las bibliotecas y módulos.
from flask import Flask
from config import config
from routes import User
from routes import System

# Crea una nueva instancia de Flask.
app = Flask(__name__)


# Define el manejador de error para el error 404 (página no encontrada).
def page_not_found(error):
    return "<h1>Not found page</h1>", 404


# Comprueba si este archivo se está ejecutando directamente y no está siendo importado.
if __name__ == "__main__":
    # Configura la aplicación con la configuración de desarrollo.
    app.config.from_object(config["development"])
    # Registra el blueprint para las rutas de usuarios.
    app.register_blueprint(User.main, url_prefix="/usuarios")
    # Registra el blueprint para las rutas del sistema.
    app.register_blueprint(System.main, url_prefix="/estado")
    # Registra el manejador de error para el error 404.
    app.register_error_handler(404, page_not_found)
    # Inicia la aplicación.
    # app.run()
    app.run(host='0.0.0.0', port=5000)
