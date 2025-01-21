from flask import Flask
from flask import render_template, request, redirect, Response, url_for, session
from flask_mysqldb import MySQL,MySQLdb 


app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'l1-login'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
print('app.config complete')
# initialize MySQL
mysql = MySQL(app)
if mysql:
    print('MySQL initialized successfully')

@app.route('/')
def home():
    return render_template('index.html')   

@app.route('/volver-ingresar')
def volverIngresar():
    return render_template('index.html')   

@app.route('/admin')
def admin():
    return render_template('admin.html')   

@app.route('/acceso-login', methods= ["GET", "POST"])
def login():
   
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
       
        _username = request.form['username']
        _password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (_username , _password,))
        account = cur.fetchone()
      
        if account:
            session['logueado'] = True
            session['id'] = account['id']

            return render_template("admin.html")
        else:
            return render_template('index.html',mensaje="User and password not found")

    
if __name__ == '__main__':
   app.secret_key = "pinchellave"
   app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
