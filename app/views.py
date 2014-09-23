#!flask/bin/python
from app import app, parser
from flask import request, flash, redirect, url_for, render_template, send_from_directory
from werkzeug import secure_filename
import os

upload_folder = 'app/uploads/'
app.config['upload_folder'] = upload_folder
new_filename = 'upload.txt'
allowed_extensions = set(['txt'])

import re, os
chat = {}
chat_history = open('app/uploads/upload.txt', 'r')

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
            return redirect(url_for('parse'))
    return render_template('index.html')

@app.route('/parsed')
def parse():
    for line in chat_history:
        string = line
        line = re.split(r'\t+', string)
        date = line[0]
        time = line[1]
        timestamp = date + time
        participant = line[4]
        direction = line[2]
        if direction == 'in':
            sender = participant
        else:
            sender = 'You'
            data = line[5]
        if chat.has_key(sender):
            message = [timestamp, data]
            chat[sender].append(message)
        else:
            chat[sender] = []
            message = [timestamp, data]
            chat[sender].append(message)
    print chat
    return render_template('parsed.html')