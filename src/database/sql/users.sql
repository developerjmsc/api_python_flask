/*
Instrucción SQL para crear la tabla de usuarios en PostgreSQL.

La tabla 'users' se utiliza para almacenar información de usuarios, incluidos detalles como su identificación,
nombre, apellidos y fecha de nacimiento.

Estructura de la tabla:
- id: Clave primaria única en formato UUID (string de 36 caracteres) que identifica a cada usuario.
- cedula_identidad: Número de cédula de identidad del usuario (hasta 20 caracteres).
- nombre: Nombre del usuario (hasta 100 caracteres).1
- primer_apellido: Primer apellido del usuario (hasta 00 caracteres).
- segundo_apellido: Segundo apellido del usuario (hasta 100 caracteres).
- fecha_nacimiento: Fecha de nacimiento del usuario en formato DATE.

Instrucción SQL:
*/

CREATE TABLE users (
    id UUID PRIMARY KEY,
    cedula_identidad VARCHAR(20),
    nombre VARCHAR(100),
    primer_apellido VARCHAR(100),
    segundo_apellido VARCHAR(100),
    fecha_nacimiento DATE
);
