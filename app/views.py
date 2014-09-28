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
            return redirect(url_for('display_dashboard'))
        else:
            flash ('Please upload a .txt file.')
            return redirect('/')
    return render_template('upload.html')

@app.route('/dashboard')
def display_dashboard():
    chat = parse()
    messages = {}
    byDates = {}
    for key in chat:
        number = len(chat[key])
        messages[key] = number
        # construct messages per month by year and month
        for i in range(0, len(chat[key])):
            yearMonth = chat[key][i][0].split(" ")[0][:7]
            if yearMonth in byDates:
                if key in byDates[yearMonth]:
                    byDates[yearMonth][key]+=1
                else:
                    byDates[yearMonth][key]={}
                    byDates[yearMonth][key]=1
            else:
                byDates[yearMonth]={}
                byDates[yearMonth][key]={}
                byDates[yearMonth][key]=1

    print messages
    return render_template('dashboard.html', messages=messages, dateGraph=byDates)