from venv import create
from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3
import os
from werkzeug.utils import secure_filename

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

import logic

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
db.init_app(app)
db.app = app
app.secret_key = "secret"
UPLOAD_FOLDER = 'static/files'

conn = sqlite3.connect('database.db', check_same_thread = False)
ALLOWED_EXTENSIONS = set(['.txt', '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.docx', '.stl']) #configure later
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ARCHIVED_FOLDER'] = "static/archived_files"

login_manager = LoginManager(app)
login_manager.login_view = 'archive'
# login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    def __repr__(self):
        return '<User %r>' % self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db.create_all()
db.session.commit()


@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        passw = request.form['password']
        appr = logic.checkEmail(email) # is approved, id
        if appr[0]:
            print("a")
            if check_password_hash(logic.getPassHash(email), passw):
                print("b")

                print("-------------------------")
                print("--- successful login! ---")
                print("-------------------------")

                usr = User.query.filter_by(id=appr[1]).first()
                print(usr)

                login_user(usr, remember=True)

                print("logged in finally!")
                return redirect('/logged_in')

            else:
                flash("invalid username or password", "error")
                return redirect('/login')
        else:
            print("-------------------------")
            print("--- mod not approved! ---")
            print("-------------------------")
            return redirect('/login')

    else:
        return render_template('login.html')
        
@app.route('/logged_in', methods = ["GET", "POST"])
@login_required
def loggedin():
    if request.method == 'POST':
        pass
    else:
        return render_template('loggedin.html')

@app.route('/approve-mod', methods = ['GET', 'POST'])
@login_required
def approve():
    if request.method == 'POST':
        email = request.form['email']
        conn.execute("UPDATE moderator SET isapproved = 1 WHERE email = ?", ((email), ))
        conn.commit()
        idthing = int(conn.execute("SELECT id FROM moderator WHERE email = ?", ((email),)).fetchone()[0])
        newmod = User(email = email, id = idthing)
        db.session.add(newmod)
        db.session.commit()
    else:
        return render_template("approve.html")

@app.route('/sign-up', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        passwHash = generate_password_hash(request.form['password'], method = "sha256")
        
        conn.execute("INSERT INTO moderator values (NULL, ?, ?)", (email, passwHash))
        conn.commit()
        
    else:
        pass
def createAndAuth(email, passw):
    conn.execute("INSERT INTO moderator values (NULL, ?, ?, ?)", ((email), (generate_password_hash(passw, method="sha256")), (1)))
    conn.commit()
    idthing = int(conn.execute("SELECT id FROM moderator WHERE email = ?", ((email),)).fetchone()[0])
    newmod = User(email = email, id = idthing)
    db.session.add(newmod)
    db.session.commit()

#####################################

@app.route('/', methods = ['GET'])
def index():
    # logic.printAllSubjects()
    # logic.processInfo("")
    logic.getAllCells("english")
    logic.getAllCells("math")
    logic.getAllCells("science")
    
    return render_template('index.html')

def wipeAccounts():
    conn.execute("DELETE FROM moderator")
    conn.commit()
    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()

@app.route('/archive', methods = ['GET'])
def archive():
    # logic.wipeRows()
    # logic.wipeSubjects()
    # logic.wipeEverything()
    # logic.printAllRows()
    info = logic.getEverything()
    # wipeAccounts()
    
    
    # createAndAuth("25benjaminli@gmail.com", "test")
    print(conn.execute("SELECT * FROM moderator").fetchall())

    return render_template('archive.html', info = info)
# @app.route('/archive-test', method = ['GET', 'POST'])
# def archivetest():
    

@app.route('/resources', methods = ['GET'])
def resources():
    return render_template('resources.html')

@app.route('/submit-item', methods = ['GET', 'POST'])
def submit():
    # logic.wipeRows()
    if request.method == 'POST':
        subject = request.form['subject']
        title = request.form['title']
        url = request.form['url']
        typ = request.form['type']
        contributors = request.form['contributors']
        print(subject, title, typ, contributors)
        # create a row under the specified subject.
        logic.processInfo(subject, title, url, typ, contributors)
        return redirect('/archive')
    elif request.method == 'GET':
        return render_template('submit-item.html')


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)

