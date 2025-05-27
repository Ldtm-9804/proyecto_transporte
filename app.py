### app.py ###

import os
from flask import Flask
import mysql.connector
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de base de datos
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'root')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'transporte_db')

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

# Registrar el blueprint
from routes.usuarios import usuarios_bp
app.register_blueprint(usuarios_bp)

if __name__ == "__main__":
    app.run(debug=True)


### routes/usuarios.py ###

from flask import Blueprint, render_template, request, redirect, url_for
from app import get_db_connection

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def inicio():
    return "Bienvenido a la automatización del transporte público"

@usuarios_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        tipo = request.form['tipo_usuario']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO Usuario (nombre, correo, contrasena, tipo_usuario)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, correo, contrasena, tipo))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('usuarios.inicio'))
        except Exception as e:
            return f"Error al registrar el usuario: {e}"

    return render_template('registro.html')
