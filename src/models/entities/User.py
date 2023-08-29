from utils.DateFormat import DateFormat


class User:
    """
    Clase que representa un usuario.

    Atributos:
    - id (str): Identificador único del usuario (UUID en formato de cadena).
    - cedula_identidad (str): Número de cédula de identidad del usuario.
    - nombre (str): Nombre del usuario.
    - primer_apellido (str): Primer apellido del usuario.
    - segundo_apellido (str): Segundo apellido del usuario.
    - fecha_nacimiento (str): Fecha de nacimiento del usuario en formato de cadena (YYYY-MM-DD).
    """

    def __init__(
        self,
        id,
        cedula_identidad=None,
        nombre=None,
        primer_apellido=None,
        segundo_apellido=None,
        fecha_nacimiento=None,
    ):
        """
        Constructor de la clase User.

        Parámetros:
        - id (str): Identificador único del usuario (UUID en formato de cadena).
        - cedula_identidad (str, opcional): Número de cédula de identidad del usuario.
        - nombre (str, opcional): Nombre del usuario.
        - primer_apellido (str, opcional): Primer apellido del usuario.
        - segundo_apellido (str, opcional): Segundo apellido del usuario.
        - fecha_nacimiento (str, opcional): Fecha de nacimiento del usuario en formato de cadena (YYYY-MM-DD).
        """
        self.id = id
        self.cedula_identidad = cedula_identidad
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento

    def to_JSON(self):
        """
        Convierte el objeto User a un diccionario JSON.

        Retorna:
        dict: Diccionario JSON con los atributos del usuario.
        """
        return {
            "id": self.id,
            "cedula_identidad": self.cedula_identidad,
            "nombre": self.nombre,
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "fecha_nacimiento": DateFormat.convert_date(self.fecha_nacimiento),
        }
