from database.db import get_connection
from .entities.User import User


class UserModel:
    """
    Modelo de base de datos para la entidad User.
    Proporciona métodos para interactuar con la tabla 'users' en la base de datos.

    Métodos de Clase:
    - all(): Recupera todos los usuarios de la base de datos.
    - find(id): Busca un usuario por su id en la base de datos.
    - store(user): Agrega un nuevo usuario a la base de datos.
    - update(user): Actualiza un usuario existente en la base de datos.
    - delete(user): Elimina un usuario de la base de datos.
    """

    @classmethod
    def all(self):
        """
        Recupera todos los usuarios de la base de datos.

        Retorna:
        list: Lista de diccionarios JSON representando usuarios.
        """
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM users ORDER BY cedula_identidad ASC"
                )
                resultset = cursor.fetchall()
                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def find(self, id):
        """
        Busca un usuario por su id en la base de datos.

        Parámetros:
        id (str): id del usuario a buscar.

        Retorna:
        dict or None: Diccionario JSON representando el usuario encontrado, o None si no se encontró.
        """
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM users WHERE id = %s",
                    (id,),
                )
                row = cursor.fetchone()
                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def averageAge(self):
        """
        Calcula el promedio de edades de todos los usuarios en la base de datos.

        Retorna:
        dict: Un diccionario con la clave 'promedio_edad' y el valor del promedio de edades calculado.
        """
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT AVG(EXTRACT(YEAR FROM AGE(NOW(), fecha_nacimiento))) as promedio_edad FROM users"
                )
                row = cursor.fetchone()

            connection.close()
            return row[0]
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def store(self, user):
        """
        Agrega un nuevo usuario a la base de datos.

        Parámetros:
        user (User): Objeto User a agregar a la base de datos.

        Retorna:
        int: Número de filas afectadas en la base de datos.
        """
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES(%s,%s,%s,%s,%s,%s)",
                    (
                        user.id,
                        user.cedula_identidad,
                        user.nombre,
                        user.primer_apellido,
                        user.segundo_apellido,
                        user.fecha_nacimiento,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex

    @classmethod
    def update(self, user):
        """
        Actualiza un usuario existente en la base de datos.

        Parámetros:
        user (User): Objeto User con los nuevos datos a actualizar.

        Retorna:
        int: Número de filas afectadas en la base de datos.
        """
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE users SET cedula_identidad = %s, nombre = %s, primer_apellido = %s, segundo_apellido = %s, fecha_nacimiento = %s WHERE id = %s",
                    (
                        user.cedula_identidad,
                        user.nombre,
                        user.primer_apellido,
                        user.segundo_apellido,
                        user.fecha_nacimiento,
                        user.id,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex

    @classmethod
    def delete(self, user):
        """
        Elimina un usuario de la base de datos.

        Parámetros:
        user (User): Objeto User a eliminar de la base de datos.

        Retorna:
        int: Número de filas afectadas en la base de datos.
        """
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex
