from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_mysqldb import MySQL
from conexion import config
from flask_login import LoginManager,login_user,logout_user,login_required
from flask_wtf.csrf import CSRFProtect
#MODELS:
from models.ModelUser import ModelUser

#ENTITIES:
from models.entities.User import User

csrf=CSRFProtect()

app = Flask(__name__)
app.config['TESTING'] = False
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def loaduser(id):
    return ModelUser.get_by_id(db,id)

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Pagina no encontrada.</h1>"


@app.route('/')
def index():
    return redirect(url_for('login'))



@app.route('/home')
@login_required
def home():

    cur = db.connection.cursor()
    cur.execute("SELECT * FROM registros ORDER BY id DESC")
    data = cur.fetchall()
    return render_template('index.html', data = data)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta vista es solo para usuarios.</h1>"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form['username']

        password = request.form['password']
        
        user = User(0, username,0,password)
        logged_user = ModelUser.login(db,user)
        
        if logged_user !=None:
            
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))

            else:
                flash("Contraseña incorrecta.")
                return render_template('login.html')
        else:
            flash("Usuario no encontrado.")

    return render_template('login.html')

if __name__ == "__main__":
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()