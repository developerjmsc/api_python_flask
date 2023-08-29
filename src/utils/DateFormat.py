# Importa el módulo datetime para trabajar con fechas y horas.
import datetime


# Define una clase DateFormat para manejar formatos de fechas.
class DateFormat:
    # Define un método de clase que convierte una fecha a un formato específico.
    @classmethod
    def convert_date(self, date):
        # Usa la función strftime para convertir la fecha a un formato de cadena.
        # El formato "%d/%m/%Y" significa que la fecha se mostrará como "día/mes/año".
        return datetime.datetime.strftime(date, "%d/%m/%Y")
