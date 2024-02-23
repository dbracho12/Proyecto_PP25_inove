import traceback
from flask import Flask, request, jsonify,render_template, Request, redirect, url_for
#Base de datos
from flask_sqlalchemy import SQLAlchemy

#Server Flask
app = Flask(__name__)

#Indicar de donde leer la base de dato
app.config["SQLALCHEMY_DATABASE_URI"] = "SQLLITE:///posteos.db"

db = SQLAlchemy()
db.init_app(app)

#---------------- Crear Tabla de la base de dato--------------------- #
class Posteos(db.Model):
    __tablename__ = "posteos"
    id = db.Column(db.Interger,primary_key = True,)
    usuario = db.Column(db.String)
    titulo = db.Column(db.String)
    texto = db.Column(db.String)

    def __repr__(self):
        return f"Usuario : {self.usuario} Titulo : {self.titulo} Texto : {self.texto}"
    
#---------------- Crear las Rutas o Endpoints del Frontend----------------- #
    # 1) Endpoint de Bienvenida o index (/)#
@app.route("/")
def index():
    try:
        #Renderizar el template HTML blog.html
        return render_template('blog.html')
    except:
        #En caso de falla
        return jsonify({'trace': traceback.format_exc()})
  
    # 2) Endpoint login (/login)#
@app.route("/login")
def logearse():
    try:
       #Renderizar el template HTML blog.html
        return render_template('login.html') 
    
    except:
        return jsonify({'trace': traceback.format_exc()})






# Este método se ejecutará la primera vez
# cuando se construye la app.
with app.app_context():
    db.create_all()
    print('Base de dato Creada')

if __name__ =='__main__':
    print('¡Provecto final del curso PP25 start!')
app.run(host="172.0.0.1", port=5000)    