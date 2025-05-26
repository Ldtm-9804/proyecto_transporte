# routes/usuarios.py

from flask import Blueprint, render_template, request, redirect, url_for
from db import get_db_connection  # <--- ahora importamos desde db.py

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
