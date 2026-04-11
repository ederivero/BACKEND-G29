from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv
from sqlalchemy import Column, types
from flask_cors import CORS

# leera el archivo .env y las variables declaradas en ese archivo las colocara como variables de entorno del sistema
load_dotenv()

app = Flask(__name__)
# se guarda todas las variables que necesita Flask para poder funcionar
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# origins > se coloca todos los origenes permitidos que pueden acceder a mi api 
# headers > headers permitidos (por defecto son todos)
# methods > methodos permitidos para acceder (por defecto son todos)
CORS(app=app, origins=['http://127.0.0.1:5600', 'http://127.0.0.1:5500'])


# Crear la conexion a la bd
conexion = SQLAlchemy(app=app)

# Inicializamos la clase de la migraciones con la instancia de Flask y la instancia de SQLAlchemy
Migrate(app=app, db=conexion)


# Aca crearemos los modelos
class CanchaModel(conexion.Model):
    # Al momento de crear la tabla en la bd usando el ORM se pueda identificar los atributos que tambien van a ser columnas en la tabla en la bd
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#
    # https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column.params.name
    
    # id SERIAL PRIMARY KEY
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    # nombre TEXT NOT NULL
    nombre = Column(type_=types.Text, nullable=False)

    # para modificar el nombre a la tabla 
    __tablename__ = 'canchas'


@app.route('/canchas', methods = ['GET', 'POST'])
def manejoCanchas():
    if request.method == 'POST':
        # Para crear un nuevo registro de la cancha 
        data = request.get_json()
        nuevaCancha = CanchaModel(nombre = data.get('nombre'))

        # Asi agregamos un nuevo registro a nuestra tabla
        conexion.session.add(nuevaCancha)

        # Para que este cambio se mantenga de manera permanente 
        conexion.session.commit()

        return {
            'message':'Cancha creada exitosamente'
        }, 201
    
    elif request.method == 'GET':
        # obtener informacion de la base de datos mediante el ORM
        # SELECT * FROM canchas;
        canchas = conexion.session.query(CanchaModel).all()
        resultado = []

        # itero los registros devueltos por la base de datos y los convierto a un formato legible para ser devueltos
        for cancha in canchas:
            resultado.append({
                'id': cancha.id,
                'nombre':cancha.nombre
            })

        return {
            'message':'Las canchas son',
            'content': resultado
        }

if __name__ == "__main__":
    app.run(debug=True)