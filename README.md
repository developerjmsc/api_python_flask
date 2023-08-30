# API REST de Administración de Usuarios

Esta API REST permite administrar usuarios y proporciona varios endpoints para realizar operaciones relacionadas con ellos.

---

## Configuración del Entorno

Antes de utilizar la API, asegúrate de configurar la base de datos y crear la tabla necesaria. Puedes usar el siguiente SQL para crear la tabla `users`:

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    cedula_identidad VARCHAR(20),
    nombre VARCHAR(100),
    primer_apellido VARCHAR(100),
    segundo_apellido VARCHAR(100),
    fecha_nacimiento DATE
);

-- Ejemplo 1
INSERT INTO users (id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
VALUES ('2a543f41-c73e-4849-b6cf-a02dec6481dc', '123456789', 'Usuario 1', 'Apellido 1', 'Apellido 2', '2000-01-01');

-- Ejemplo 2
INSERT INTO users (id, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
VALUES ('f71ef553-86c4-4a0a-ad25-112008de7d0b', '987654321', 'Usuario 2', 'Apellido 3', 'Apellido 4', '1995-05-10');
```

Asegúrate de realizar los siguientes pasos:

1. Clona este repositorio en tu máquina local:

```

git clone https://github.com/jm-suarez/api_python_flask.git

```

2. Crea y configura el archivo `.env` en la raíz del proyecto con las variables de entorno requeridas.

```plaintext
SECRET_KEY=key
PGSQL_HOST=localhost
PGSQL_USER=user
PGSQL_PASSWORD=password
PGSQL_DATABASE=users

SYSTEM_NAME="API PYTHON FALSK"
SYSTEM_VERSION="0.0.1"
DEVELOPER_NAME="JOSE MARIA SUAREZ CABRERA"
DEVELOPER_EMAIL="jm.suarez.cabrera@gmail.com"
```

3. Crea un entorno virtual en la carpeta del proyecto:

```
python -m venv venv
```

4. Activa el entorno virtual:

- En Windows:
  ```
  venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

5. Instala las dependencias del proyecto:

```
pip install -r requirements.txt
```

6. Levanta el API REST:

```
python app.py
```

7. El API estará disponible en http://localhost:5000. Puedes acceder a los diferentes endpoints descritos en la documentación para realizar pruebas.

```plaintext
  ¡Listo! Ahora puedes comenzar a utilizar el API REST para administrar usuarios.
```

---

## Endpoints

1. [Recuperar Todos los Usuarios](#recuperar-todos-los-usuarios)
2. [Obtener un usuario en específico](#obtener-un-usuario-en-específico)
3. [Crear un nuevo usuario](#crear-un-nuevo-usuario)

---

### Recuperar Todos los Usuarios

Obtiene una lista de todos los usuarios registrados.

- **Método:** GET
- **Ruta:** `/usuarios`
- **Respuesta exitosa (Código 200):**

  ```json
  [
    {
      "id": "2a543f41-c73e-4849-b6cf-a02dec6481dc",
      "cedula_identidad": "123456789",
      "nombre": "Usuario 1",
      "primer_apellido": "Apellido 1",
      "segundo_apellido": "Apellido 2",
      "fecha_nacimiento": "2000-01-01"
    },
    {
      "id": "f71ef553-86c4-4a0a-ad25-112008de7d0b",
      "cedula_identidad": "987654321",
      "nombre": "Usuario 2",
      "primer_apellido": "Apellido 3",
      "segundo_apellido": "Apellido 4",
      "fecha_nacimiento": "1995-05-10"
    }
    // ... otros usuarios
  ]
  ```

- **Respuesta en Caso de Error (Código 500):**
  ```json
  {
    "message": "Ha ocurrido un error en el servidor."
  }
  ```

---

### Obtener un usuario en específico

Obtiene los detalles de un usuario específico por su ID.

- **Método:** GET
- **Ruta:** `/usuarios/<id>`
- **Respuesta exitosa (Código 200):**

```json
{
  "id": "2a543f41-c73e-4849-b6cf-a02dec6481dc",
  "cedula_identidad": "123456789",
  "nombre": "Usuario 1",
  "primer_apellido": "Apellido 1",
  "segundo_apellido": "Apellido 2",
  "fecha_nacimiento": "2000-01-01"
}
```

---

### Crear un nuevo usuario

Crea un nuevo usuario.

- **Método:** POST
- **Ruta:** `/usuarios`
- **Cuerpo de la solicitud (JSON):**

```json
{
  "cedula_identidad": "987654321",
  "nombre": "Nuevo Usuario",
  "primer_apellido": "Nuevo Apellido",
  "segundo_apellido": "Nuevo Apellido 2",
  "fecha_nacimiento": "1998-09-15"
}
```

---

### Actualizar un usuario existente

Actualiza los datos de un usuario existente por su ID.

- **Método:** PUT
- **Ruta:** `/usuarios/<id>`
- **Cuerpo de la solicitud (JSON):**

```json
{
  "cedula_identidad": "987654321",
  "nombre": "Usuario Modificado",
  "primer_apellido": "Apellido Modificado",
  "segundo_apellido": "Apellido Modificado 2",
  "fecha_nacimiento": "1985-12-20"
}
```

--

### Eliminar un usuario

Elimina un usuario existente por su ID.

- **Método:** DELETE
- **Ruta:** `/usuarios/<id>`

---

### Obtener el promedio de edades

Calcula y obtiene el promedio de edades de todos los usuarios en la base de datos.

- **Método:** GET
- **Ruta:** `/usuarios/promedio-edad`
- **Descripción:** Esta ruta calcula el promedio de edades de todos los usuarios registrados en la base de datos.

### Respuesta exitosa

- **Código:** 200
- **Ejemplo de respuesta:**
  ```json
  {
    "promedio_edad": 29.5
  }
  ```

### Respuesta en caso de error

- **Código:** 500
- **Ejemplo de respuesta:**

```json
{
  "message": "Ha ocurrido un error al calcular el promedio de edad."
}
```

---

### Obtener Información del Estado del Sistema

Este endpoint permite obtener información sobre el estado del sistema, incluyendo su nombre, versión, desarrollador y correo electrónico de contacto.

- **URL:** `/estado`
- **Método:** `GET`
- **Respuesta Exitosa:**

  - Código de Estado: 200 OK
  - Contenido:

    ```json
    {
      "nameSystem": "Nombre del Sistema",
      "version": "Versión del Sistema",
      "developer": "Nombre del Desarrollador",
      "email": "Correo Electrónico del Desarrollador"
    }
    ```

- **Respuesta en Caso de Error:**

  - Código de Estado: 500 Internal Server Error
  - Contenido:

    ```json
    {
      "message": "Ha ocurrido un error en el servidor."
    }
    ```
