# Librerias
# Flask es un microframework web para Python que permite crear aplicaciones web de forma
# sencilla, rápida y flexible. 
from flask import Flask, render_template, request, redirect

#flask_mysqldb es una extensión para Flask que permite conectar tu aplicación web escrita
# en Flask con una base de datos MySQL usando el conector MySQLdb (MySQL-python).
import mysql.connector

# Flask(__name__): Inicializa la aplicación Flask con el nombre del módulo actual, 
# lo que permite que Flask sepa dónde buscar archivos estáticos y plantillas.
app = Flask(__name__)

# Configuración de la base de datos
db = mysql.connector.connect(
    host="localhost",  # direccion server
    user="root",      # usuario de base de datos
    password="",      # contraseña de base de datos
    database="py_clientes_db"    # nombre de base de datos
)

#cursor() crea un cursor para ejecutar consultas.
#dictionary=True hace que los resultados sean diccionarios, facilitando el acceso
# a los datos por nombre de columna.
cursor = db.cursor(dictionary=True)


# Página principal con formulario
@app.route("/", methods=["GET", "POST"])
def index():
    # Recibe los datos del formulario
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]

        # Inserta datos en la tabla clientes en la BD Página
        sql = "INSERT INTO clientes (nombre, correo, telefono) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, correo, telefono))
        db.commit()

        # Esta liena le dice al navegador que realice una nueva solicitud a la URL /clientes.
        return redirect("/clientes")
    # render_template("index.html"): Busca y renderiza el archivo index.html desde el directorio
    # return: Envía la plantilla renderizada al cliente como respuesta.
    return render_template("index.html")

# Mostrar clientes en tabla
@app.route("/clientes")
def clientes():
    cursor.execute("SELECT * FROM clientes")
    data = cursor.fetchall()
    return render_template("clientes.html", clientes=data)

if __name__ == "__main__":
    app.run(debug=True)
