# Importa las bibliotecas necesarias de Flask, uuid y los modelos de usuario.
from flask import Blueprint, jsonify, request
import uuid
from models.entities.User import User
from models.UserModel import UserModel

# Crea un Blueprint para las rutas de usuario. Un Blueprint es una forma de organizar las rutas en una aplicación Flask.
main = Blueprint("user_blueprint", __name__)


# Define una ruta para "/" que recupera todos los usuarios de la base de datos.
@main.route("/")
def all():
    """
    Recupera todos los usuarios de la base de datos.

    Retorna:
    list: Lista de diccionarios JSON representando usuarios.
    """
    try:
        # Utiliza el método all() del modelo de usuario para recuperar todos los usuarios.
        users = UserModel.all()
        return jsonify(users)
    except Exception as ex:
        # Si ocurre algún error, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 500.
        return jsonify({"mesage": str(ex)}), 500


# Define una ruta para "/promedio-edad" que calcula el promedio de edad de todos los usuarios.
@main.route("/promedio-edad")
def promedio_edad():
    """
    Obtiene el promedio de edad de todos los usuarios en la base de datos.

    Retorna:
    dict: Un diccionario con la clave 'promedio_edad' y el valor del promedio de edades calculado.
    """
    try:
        # Utiliza el método averageAge() del modelo de usuario para calcular el promedio de edad.
        return jsonify({"promedio_edad": UserModel.averageAge()})
    except Exception as ex:
        # Si ocurre algún error, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 500.
        return jsonify({"message": str(ex)}), 500


# Define una ruta para "/<id>" que busca un usuario por su id.
@main.route("/<id>")
def find(id):
    """
    Busca un usuario por su id en la base de datos.

    Parámetros:
    id (str): id del usuario a buscar.

    Retorna:
    dict or 404: Diccionario JSON representando el usuario encontrado, o respuesta 404 si no se encontró.
    """
    try:
        # Utiliza el método find() del modelo de usuario para buscar el usuario por su id.
        user = UserModel.find(id)
        if user != None:
            return jsonify(user)
        else:
            # Si no se encontró el usuario, retorna un objeto JSON vacío y un código de estado HTTP 404.
            return jsonify({}), 404
    except Exception as ex:
        # Si ocurre algún error, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 500.
        return jsonify({"message": str(ex)}), 500


# Define una ruta para "/" que agrega un nuevo usuario a la base de datos. Esta ruta acepta solicitudes POST.
@main.route("/", methods=["POST"])
def store():
    """
    Agrega un nuevo usuario a la base de datos.

    Parámetros en el cuerpo de la solicitud (JSON):
    - cedula_identidad (str): Número de cédula de identidad.
    - nombre (str): Nombre del usuario.
    - primer_apellido (str): Primer apellido del usuario.
    - segundo_apellido (str): Segundo apellido del usuario.
    - fecha_nacimiento (str): Fecha de nacimiento del usuario en formato "YYYY-MM-DD".

    Retorna:
    str or 404: ID del usuario agregado, o respuesta 404 si ocurrió un error en la inserción.
    """
    try:
        # Recupera los datos del usuario del cuerpo de la solicitud.
        cedula_identidad = request.json["cedula_identidad"]
        nombre = request.json["nombre"]
        primer_apellido = request.json["primer_apellido"]
        segundo_apellido = request.json["segundo_apellido"]
        fecha_nacimiento = request.json["fecha_nacimiento"]
        # Genera un id único para el nuevo usuario.
        id = uuid.uuid4()
        # Crea un nuevo objeto de usuario con los datos recuperados y el id generado.
        user = User(
            str(id),
            cedula_identidad,
            nombre,
            primer_apellido,
            segundo_apellido,
            fecha_nacimiento,
        )
        # Utiliza el método store() del modelo de usuario para agregar el nuevo usuario a la base de datos.
        affected_rows = UserModel.store(user)
        # Si la inserción fue exitosa, retorna el id del nuevo usuario.
        if affected_rows == 1:
            return jsonify({"id": user.id})
        else:
            # Si la inserción falló, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 404.
            return jsonify({"mesage": "Error al insertar el usuario"}), 404
    except Exception as ex:
        # Si ocurre algún error, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 500.
        return jsonify({"message": str(ex)}), 500


# Define una ruta para "/<id>" que actualiza un usuario en la base de datos. Esta ruta acepta solicitudes PUT.
@main.route("/<id>", methods=["PUT"])
def update(id):
    """
    Actualiza un usuario existente en la base de datos.

    Parámetros en el cuerpo de la solicitud (JSON):
    - cedula_identidad (str): Número de cédula de identidad.
    - nombre (str): Nombre del usuario.
    - primer_apellido (str): Primer apellido del usuario.
    - segundo_apellido (str): Segundo apellido del usuario.
    - fecha_nacimiento (str): Fecha de nacimiento del usuario en formato "YYYY-MM-DD".

    Parámetros:
    id (str): id del usuario a actualizar.

    Retorna:
    str or 404: id del usuario actualizado, o respuesta 404 si el usuario no fue actualizado.
    """
    try:
        # Recupera los datos del usuario del cuerpo de la solicitud.
        cedula_identidad = request.json["cedula_identidad"]
        nombre = request.json["nombre"]
        primer_apellido = request.json["primer_apellido"]
        segundo_apellido = request.json["segundo_apellido"]
        fecha_nacimiento = request.json["fecha_nacimiento"]
        # Crea un nuevo objeto de usuario con los datos recuperados y el id proporcionado.
        user = User(
            id,
            cedula_identidad,
            nombre,
            primer_apellido,
            segundo_apellido,
            fecha_nacimiento,
        )
        # Utiliza el método update() del modelo de usuario para actualizar el usuario en la base de datos.
        affected_rows = UserModel.update(user)
        # Si la actualización fue exitosa, retorna el id del usuario actualizado.
        if affected_rows == 1:
            return jsonify({"id": user.id})
        else:
            # Si la actualización falló, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 404.
            return jsonify({"mesage": "Ningun usuario actualizado."}), 404
    except Exception as ex:
        # Si ocurre algún error, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 500.
        return jsonify({"message": str(ex)}), 500


# Define una ruta para "/<id>" que elimina un usuario de la base de datos. Esta ruta acepta solicitudes DELETE.
@main.route("/<id>", methods=["DELETE"])
def delete(id):
    """
    Elimina un usuario de la base de datos.

    Parámetros:
    id (str): id del usuario a eliminar.

    Retorna:
    str or 404: id del usuario eliminado, o respuesta 404 si el usuario no fue eliminado.
    """
    try:
        # Crea un nuevo objeto de usuario con el id proporcionado.
        user = User(id)
        # Utiliza el método delete() del modelo de usuario para eliminar el usuario de la base de datos.
        affected_rows = UserModel.delete(user)
        # Si la eliminación fue exitosa, retorna el id del usuario eliminado.
        if affected_rows == 1:
            return jsonify({"id": user.id})
        else:
            # Si la eliminación falló, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 404.
            return jsonify({"mesage": "Ningun usuario eliminado."}), 404
    except Exception as ex:
        # Si ocurre algún error, retorna un objeto JSON con un mensaje de error y un código de estado HTTP 500.
        return jsonify({"message": str(ex)}), 500
