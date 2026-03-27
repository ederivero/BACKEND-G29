CREATE DATABASE empresa;

\c empresa

CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    piso INT
);

CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombres TEXT,
    apellidos TEXT,
    departamento_id INT, -- el tipo de datos de la llave foranea debe ser el mismo que de la llave primaria

    -- Asi se crean las relaciones
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

CREATE TABLE proyectos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    responsable_id INT NULL,
    FOREIGN KEY (responsable_id) REFERENCES empleados(id)
);


\dt -- muestra todas las tablas de la base de datos

\d NOMBRE_TABLA -- muestra la configuracion de la tabla (columnas y relaciones)


INSERT INTO departamentos (nombre, piso) VALUES 
('Baristas y Calidad', 1),
('Expediciones Misti', 2),
('Mantenimiento de Huertos', 1),
('Logística y Almacén', 3);

INSERT INTO empleados (nombres, apellidos, departamento_id) VALUES 
('Alice', 'Vargas', 1),   -- Baristas
('Bruno', 'Díaz', 1),    -- Baristas
('Carla', 'Mendoza', 2), -- Expediciones
('David', 'Torres', 3),  -- Huertos
('Elena', 'Paz', NULL);  -- Freelance (Sin departamento)

INSERT INTO proyectos (nombre, responsable_id) VALUES 
('Optimización de Espresso', 1),
('Ruta Norte del Pichu Pichu', 3),
('Sistema de Riego Vertical', 4),
('Cosecha de Café Especial', NULL);



SELECT * 
FROM departamentos AS dpto LEFT JOIN empleados AS emp 
ON dpto.id = emp.departamento_id -- sirve para indicar que columnas vamos a relacionar entre la tabla empleados y departamentos
;

SELECT * 
FROM departamentos AS dpto RIGHT JOIN empleados AS emp 
ON dpto.id = emp.departamento_id;


SELECT * 
FROM departamentos AS dpto INNER JOIN empleados AS emp 
ON dpto.id = emp.departamento_id;




-- 1. LISTAR EL NOMBRE Y APELLIDOS DE LOS EMPLEADOS Y SU NOMBRE DEL DEPARTAMENTO
SELECT emp.nombres, emp.apellidos, dpto.nombre 
FROM empleados AS emp 
            INNER JOIN departamentos AS dpto ON emp.departamento_id = dpto.id;

-- 2. MOSTRAR TODOS LOS EMPLEADOS (NOMBRES Y APELLIDOS) Y EL NOMBRE DE SUS DEPARTAMENTOS (NO IMPORTA SI EL EMPLEADO TIENE O NO DPTO)
SELECT emp.nombres, emp.apellidos, dpto.nombre 
FROM empleados AS emp 
            LEFT JOIN departamentos AS dpto ON emp.departamento_id = dpto.id;

-- 3. MOSTRAR TODOS LOS DEPARTAMENTOS QUE NO TENGAN EMPLEADOS
SELECT dpto.nombre 
FROM departamentos AS dpto LEFT JOIN empleados AS emp ON dpto.id = emp.departamento_id
-- Si queremos los dptos que no tengan empleados entonces el id del empleado sera nulo porque no hay
WHERE emp.id IS null;

-- 4. LISTAR TODOS LOS PROYECTOS Y EL NOMBRE DEL EMPLEADO
SELECT proy.nombre, emp.nombres
FROM proyectos AS proy LEFT JOIN empleados AS emp 
ON proy.responsable_id = emp.id;


-- 5. MOSTRAR EL NOMBRE DEL PROYECTO, NOMBRE Y APELLIDO DEL EMPLEADO Y NOMBRE DEL DEPARTAMENTO

-- 6. MOSTRAR EL NOMBRE DE LOS PROYECTOS DEL DEPARTAMENTO UBICADO EN EL PISO 1
