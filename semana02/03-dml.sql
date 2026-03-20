CREATE DATABASE inventario;

\c inventario

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    categoria TEXT,
    stock INT DEFAULT 0,
    precio DECIMAL(10,2),
    estado TEXT DEFAULT 'disponible'
);

INSERT INTO productos (nombre, categoria, stock, precio, estado) VALUES
('Laptop Gamer', 'Computación', 5, 1200.00, 'disponible'),
('Mouse Inalámbrico', 'Accesorios', 50, 25.50, 'disponible'),
('Monitor 24 pulgadas', 'Computación', 12, 180.00, 'disponible'),
('Teclado Mecánico', 'Accesorios', 0, 85.00, 'agotado'),
('Memoria RAM 16GB', 'Componentes', 20, 75.00, 'disponible'),
('Disco Duro 1TB', 'Componentes', 8, 50.00, 'disponible'),
('Cable HDMI 2m', 'Accesorios', 100, 10.00, 'disponible'),
('Silla Ergonómica', 'Muebles', 3, 250.00, 'disponible');

-- UPDATE
UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse Inalámbrico';

-- Cambiar el estado a 'no disponible' cuando el stock sea 0
UPDATE productos SET estado = 'no disponible' WHERE stock = 0;



-- TRANSACCIONES
-- Indicamos que vamos a empezar una transaccion
BEGIN;
UPDATE productos SET precio = 30.00;

-- Si quisieramos dejar sin efecto las modificaciones, inserciones o eliminaciones
ROLLBACK;

-- Indicamos que todas las acciones en la transaccion esta ok y queremos guardarlas de manera permanente
COMMIT;

-- DELETE
DELETE FROM productos WHERE id = 7;


-- SELECT

-- Para poner el alias se usa AS
-- Tambien es opcional y solo con un espacio de por medio
SELECT nombre, precio AS costo_unitario FROM productos;

SELECT nombre, precio AS costo_unitario 
FROM productos 
WHERE precio > 40.00;

-- WHERE se puede poner 
-- > (Mayor que), 
-- >= (Mayor o igual que),
-- < (Menor que), 
-- <= (Menor o igual que),
-- = (Igual que), 
-- != o <> (Diferente de) tambien se puede utilizar

-- Se puede utilizar el operador AND y OR
SELECT nombre, precio AS costo_unitario 
FROM productos 
WHERE precio > 40.00 AND precio < 80.00;

SELECT * 
FROM productos
ORDER BY id ASC; -- DESC

-- Se pueden agregar varios ordenamientos si se repite 
SELECT * 
FROM productos
ORDER BY categoria ASC, nombre DESC;

-- Paginacion
SELECT *
FROM productos
LIMIT 2
OFFSET 20;



CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo TEXT,
    autor TEXT,
    genero TEXT,
    precio DECIMAL(10,2),
    stock INT
);

INSERT INTO libros (titulo, autor, genero, precio, stock) VALUES
('El Quijote', 'Cervantes', 'Clásico', 25.00, 10),
('Cien años de soledad', 'García Márquez', 'Realismo', 30.00, 5),
('1984', 'George Orwell', 'Distopía', 15.00, 20),
('Fahrenheit 451', 'Ray Bradbury', 'Distopía', 12.50, 0),
('El Aleph', 'Jorge Luis Borges', 'Ficción', 22.00, 8),
('Crónica de una muerte anunciada', 'García Márquez', 'Realismo', 18.00, 12),
('Fundación', 'Isaac Asimov', 'Ciencia Ficción', 40.00, 15),
('Yo, Robot', 'Isaac Asimov', 'Ciencia Ficción', 20.00, 3);

-- Mostrar todos los libros que el genero sea Ciencia Ficcion
SELECT * 
FROM libros 
WHERE genero = 'Ciencia Ficción';

-- Mostrar todos los libros que cuesten mas de 20.00 y que tengan stock
SELECT * 
FROM libros
WHERE precio > 20.00 AND stock <> 0;