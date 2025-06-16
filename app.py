from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

db= MySQL(app)

app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")


@app.route("/add_sql",methods=["POST"])
def add_sql():


    especie = request.json["especie"]
    genero = request.json["genero"]
    color = request.json["color"]
    edad = request.json["edad"]



    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO animales (especie,genero,color,edad) VALUES (%s,%s,%s,%s)",(especie,genero,color,edad))
    db.connection.commit()

    return "Se ha añadido correctamente..."

@app.route("/get_sql",methods=["GET"])
def get_sql():

    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM animales")
    animales = cursor.fetchall()

    return jsonify(animales)



@app.route("/get_sql/<int:id>",methods=["GET"])
def get_sql_id(id):

    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM animales where id=%s",(id,))
    animal= cursor.fetchone()

    return jsonify(animal)



@app.route("/put_sql/<int:id>",methods=["PUT"])
def put_sql_id(id):


    
    especie = request.json["especie"]
    genero = request.json["genero"]
    color = request.json["color"]
    edad = request.json["edad"]



    cursor = db.connection.cursor()
    cursor.execute("UPDATE animales SET especie=%s,genero=%s,color=%s,edad=%s where id=%s",(especie,genero,color,edad,id))
    db.connection.commit()
    

    return "Actualizado con exito..."




@app.route("/delete_sql/<int:id>",methods=["DELETE"])
def delete_sql_id(id):


    

    cursor = db.connection.cursor()
    cursor.execute("DELETE from animales where id=%s",(id,))
    db.connection.commit()
    

    return "Eliminado con exito..."


if __name__ == "__main__":
    app.run(debug=True)