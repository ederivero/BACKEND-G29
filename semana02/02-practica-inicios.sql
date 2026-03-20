-- Crear base de datos llamada viajes 
CREATE DATABASE viajes;

\c viajes
-- Usando la base de datos viajes crear la tabla destinos con las siguientes columnas
-- id SERIAL y llave primaria
-- ciudad TEXTO y no puede ser nulo
-- pais TEXTO y no puede ser nulo
-- codigo_postal TEXTO y es unico
-- puntuacion ENTERO 
-- fecha_registro TIMESTAMP
CREATE TABLE destinos (
    id SERIAL PRIMARY KEY,
    ciudad TEXT NOT NULL,
    pais TEXT NOT NULL,
    codigo_postal TEXT UNIQUE,
    puntuacion INT,
    fecha_registro TIMESTAMP
);

-- Luego de crear la tabla agregar una columna llamada descripcion que sera TEXT
ALTER TABLE destinos ADD COLUMN descripcion TEXT;

-- cambiar la columna puntuacion a ranking
ALTER TABLE destinos RENAME COLUMN puntuacion TO ranking;

-- Insertar:
-- ciudad: Paris
-- pais: Francia
-- codigo_postal: 75001
-- ranking: 5
INSERT INTO destinos (ciudad, pais, codigo_postal, ranking) 
VALUES ('París', 'Francia', '75001', 5);
-- ciudad: Tokio
-- pais: Japon
-- codigo_postal: 100-0001
-- ranking: 5
INSERT INTO destinos VALUES (DEFAULT, 'Tokio', 'Japón', '100-0001', 5, DEFAULT, 'Ciudad futurista');

-- mostrar solo la ciudad y el ranking
SELECT ciudad, ranking FROM destinos;

-- mostrar todas las columnas de la tabla
SELECT * FROM destinos;