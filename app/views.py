#!flask/bin/python
from app import app
from parser import parse
from flask import request, flash, redirect, url_for, render_template, send_from_directory, Response, json
from werkzeug import secure_filename
import os

upload_folder = 'app/uploads/'
app.config['upload_folder'] = upload_folder
new_filename = 'upload.txt'
allowed_extensions = set(['txt'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allowed_extensions

@app.route('/uploads')
def hello():
    return app.config['upload_folder']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print os.path
            file.save(os.path.join(app.config['upload_folder'], new_filename))
            flash ('Got it.')
            return redirect(url_for('display_parse'))
    return render_template('index.html')

@app.route('/parsed')
def display_parse():
    chat = parse()
    users = []
    for key in chat:
        users.append(key)
    print users
    return render_template('parsed.html', users=users)