from flask import Flask, request
from psycopg import connect


# Connection string (cadena de conexion)
# DIALECTO://USER:PASSWORD@HOST:PORT/DATABASE
credenciales = 'postgresql://postgres:root@127.0.0.1:5432/empresa'
conexion = connect(conninfo=credenciales)

# En la instancia de la clase le tengo que pasar como parametro la variable __name__ y esta contendra si el archivo es el archivo principal (archivo que se esta ejecutando en la terminal) para indicar que la instancia de Flask esta siendo llamada una sola vez y no varias veces, ya que eso puede dar un error de instanciacion.
servidor = Flask(__name__)


# Para crear endpoints se hacen mediante decoradores
# Todo decorador siempre debe tener una funcion que sea a la que responda
@servidor.route('/')
def inicio():
    return 'Bienvenido a mi primera API de Flask'


@servidor.route('/departamentos',methods =['GET'])
def devolverDepartamentos():
    # es el asistente que me permite manipular mis datos en la bd
    cursor = conexion.cursor()

    # ejecutamos la consulta que deseamos 
    info = cursor.execute('SELECT * FROM departamentos')

    # fetch obtenemos los resultados de la consulta, si es un insert o un update no nos dara nada
    resultado = cursor.fetchall()
    cursor.close()
    # para obtener el nombre de las columnas de mi consulta 
    # FORMA 1 (Corta)
    columnas = [col.name for col in info.description]
    
    # FORMA 2 (Larga)
    # es lo mismo pero mas largo
    # columnas = []
    # for col in info.description:
    #     columnas.append(col.name)
    
    respuesta = []
    for registro in resultado:
        departamento = {}

        for posicion in range(len(registro)):
            departamento[columnas[posicion]] = registro[posicion]
        
        respuesta.append(departamento)
        

    return {
        'content':respuesta
    }


@servidor.route('/departamento', methods = ['POST'])
def crearDepartamento():
    # {"nombre":"Club de Juegos", "piso": 3}
    data = request.get_json()

    cursor = conexion.cursor()
    cursor.execute("INSERT INTO departamentos (nombre, piso) VALUES (%s, %s)",(data.get('nombre'), data.get('piso')))

    # Commit los cambios quedan guardados de manera permanente en la bd
    conexion.commit()

    # Siempre hay que cerrar el cursos para evitar dejar conexiones abiertas
    cursor.close()
    return {
        'message': 'Departamento creado exitosamente'
    }, 201


@servidor.route('/departamento/<id>', methods =['GET'])
def devolverDepartamento(id):
    cursor = conexion.cursor()

    info = cursor.execute("SELECT * FROM departamentos WHERE id = %s", (id,))

    data = cursor.fetchone()

    columnas = [col.name for col in info.description]

    if data:
        resultado = {}
        for posicionColumna in range(len(columnas)):
            resultado[columnas[posicionColumna]] = data[posicionColumna]

        return {
            'content': resultado
        }
    else:
        # data = None
        return {
            'message':'El departamento no existe'
        },400

@servidor.route('/buscar-departamentos', methods = ['GET'])
def buscarDepartamentos():
    # los query params en Flask
    queryParams = request.args
    print(queryParams)

    cursor = conexion.cursor()
    if queryParams.get('piso'):
        piso = queryParams.get('piso')
        info = cursor.execute('SELECT * FROM departamentos WHERE piso = %s', (piso,))
        data = cursor.fetchall()
        
        columnas = [col.name for col in info.description]

        respuesta = []
        for registro in data:
            departamento = {}

            for posicion in range(len(registro)):
                departamento[columnas[posicion]] = registro[posicion]
            
            respuesta.append(departamento)
        return {
            'content': respuesta
        }
    
    return {
        'content':''
    }


@servidor.route('/registro', methods = ['POST'])
def registroUsuario():
    # Las comunicacion mas comun en el body del backend es por JSON
    # JSON > JavaScript Object Notation (Notation del Objeto de JavaScript) en el cual el formato es mediante llave-valor, similar en python a los diccionarios
    
    # request > peticion (toda la data de esa peticion)
    # get_json() > convierte el body en bytes a un diccionario si es viable
    data = request.get_json()

    # get es un metodo de los diccionarios en el cual sirve para devolver un valor de su llave y si no existe retornara None (vacio)
    print(data.get('nombre'))
    # Si respondemos con dos parametros, el primero sera el cuerpo y el segundo sera el estado de respuesta, esto se puede poner dentro de una tupla para mejor entendimiento
    return ({
        'message':'Usuario creado exitosamente'
    },201)


# Para inicializar el servidor se puede utilizar esa variable
if __name__ == '__main__':
    print('Servidor corriendo exitosamente')
    # Si colocamos debug = True significa que siempre que guardemos algun cambio se reiniciara el servidor de manera automatica, su valor por defecto es False
    servidor.run(debug=True)