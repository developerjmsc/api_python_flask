"""
Este módulo proporciona una función para establecer una conexión a una base de datos PostgreSQL utilizando psycopg2.

Requiere la biblioteca psycopg2 y decouple para cargar las variables de entorno de configuración.

Las siguientes variables de entorno deben configurarse en un archivo .env o de otra manera antes de usar este módulo:
- PGSQL_HOST: La dirección del host de la base de datos PostgreSQL.
- PGSQL_USER: El nombre de usuario para autenticarse en la base de datos.
- PGSQL_PASSWORD: La contraseña para autenticarse en la base de datos.
- PGSQL_DATABASE: El nombre de la base de datos a la que conectarse.
"""

import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    """
    Establece una conexión a la base de datos PostgreSQL utilizando los valores de configuración
    proporcionados en las variables de entorno.

    Returns:
        psycopg2.extensions.connection: Objeto de conexión a la base de datos.

    Raises:
        DatabaseError: Si ocurre algún error al establecer la conexión.
    """
    try:
        return psycopg2.connect(
            host=config("PGSQL_HOST"),
            user=config("PGSQL_USER"),
            password=config("PGSQL_PASSWORD"),
            database=config("PGSQL_DATABASE"),
        )
    except DatabaseError as ex:
        raise ex
