-- Este comando es de psql , no de sql y por ende solo se puede usar en bd de Postgres
-- Sirve para listar las bases de datos que existen en el servidor
\l

-- DDL (Data Definition Language) SUS acciones son
-- CREATE: Crear bases de datos o tablas o indices o algun componente que sea para la base de datos
-- ALTER: Modificar alguna propiedad de la base de datos
-- DROP: Eliminar de manera permanente
-- TRUNCATE: Elimina la data de una tabla sin eliminar su configuracion
-- RENAME: Cambiar el nombre a las entidades
CREATE DATABASE pruebas;

-- Cambiarse a otra base de datos que exista
\c 


CREATE TABLE personas (
    -- llave primaria | (no) acepte nulos | valor unica | valor por defecto
    -- PRIMARY KEY    | NULL   | NOT NULL | UNIQUE     | DEFAULT 
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT,
    correo TEXT UNIQUE,
    fecha_nacimiento TIMESTAMP
);


-- Usando el comando ALTER para modificar la tabla

-- Si quisieramos agregar una columna
ALTER TABLE personas ADD COLUMN nickname TEXT; -- Configuraciones adicionales: NOT NULL UNIQUE PRIMARY KEY DEFAULT 'no_nickname'

-- Eliminar una columna
ALTER TABLE personas DROP COLUMN nickname;

-- Cambiar el nombre de una columna
ALTER TABLE personas RENAME COLUMN nombre TO nombres;

-- Cambiar el tipo de dato (esto solo es valido si la columna no tiene datos o si son compatibles)
ALTER TABLE personas ALTER COLUMN nombres TYPE VARCHAR(200);


-- Muestra todas las tablas de la base de datos
\dt

-- Muestra las tablas y sus secuenciales (autoincrementables) de la base de datos 
\d



-- DML (Data Manipulation Language)
-- INSERT
-- SELECT
-- UPDATE
-- DELETE

-- Las fechas siguen el formato ISO-8601 (de mas a menos)
INSERT INTO personas (id, nombres, apellido, correo, fecha_nacimiento) VALUES 
                    (DEFAULT, 'Eduardo Ramiro', 'de Rivero', 'ederiveroman@gmail.com', '1992-08-01');

-- al no indicar las columnas si o si las tenemos que declarar todas
INSERT INTO personas VALUES (DEFAULT, 'Roxana Diana', 'Huayra', 'rhuayra@gmail.com', '2001-03-18');

-- SELECT
SELECT id, nombres FROM personas;

-- Sirve para utilizar todas las columnas
SELECT * FROM personas;