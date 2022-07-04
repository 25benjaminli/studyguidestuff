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

@app.route('/', methods = ['GET'])
def index():
    # logic.printAllSubjects()
    # logic.processInfo("")
    logic.getAllCells("english")
    logic.getAllCells("math")
    logic.getAllCells("science")


    return render_template('index.html')

@app.route('/archive', methods = ['GET'])
def archive():
    # logic.wipeRows()
    # logic.wipeSubjects()
    # logic.wipeEverything()
    # logic.printAllRows()
    info = logic.getEverything()

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

