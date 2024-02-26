import traceback
from flask import Flask, request, jsonify,render_template, Request, redirect, url_for
#Base de datos
from flask_sqlalchemy import SQLAlchemy

#Server Flask
app = Flask(__name__)

#Indicar de donde leer la base de dato
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posteos.db"

db = SQLAlchemy()
db.init_app(app)

#---------------- Crear Tabla de la base de dato--------------------- #
class Posteos(db.Model):
    __tablename__ = "posteos"
    id = db.Column(db.Integer,primary_key = True,)
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

#-----------------Crear Endpoinds del Backkend ------------------------------#
@app.route("/usuario/<nombre>")
def usuario(nombre):
    try:
        # Renderizar el temaplate HTML user.html
        
        return render_template('blog.html', usuario=nombre)
    except:
        return jsonify({'trace': traceback.format_exc()})
    
@app.route("/", methods=['GET','POST'])
def u():
    
    if request.method == 'GET':
        try:
            nombre = nombre.lower()


            query = db.session.query(Posteos).filter(Posteos.titulo,Posteos.texto).order_by(Posteos.usuario.desc())
            query =query.limit(3)

            datos = []
            for dato in query:
                dato_json = {}
                dato_json['titulo']= dato.titulo
                dato_json['texto'] = dato.texto
                datos.append(dato_json)


            return jsonify(datos)

        except:
            return jsonify({'trace': traceback.format_exc()})
    
    #if request.method == 'POST':
        







# Este método se ejecutará la primera vez
# cuando se construye la app.
with app.app_context():
    db.create_all()
    print('Base de dato Creada')

if __name__ =='__main__':
    print('¡Provecto final del curso PP25 start!')
app.run(host="127.0.0.1", port=5000)    