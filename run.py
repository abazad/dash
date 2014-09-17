#!flask/bin/python
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = 'app/uploads/'
NEW_FILENAME = 'upload.txt'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads')
def hello():
    return app.config['UPLOAD_FOLDER']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # return os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], NEW_FILENAME))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>dash</title>
    <h1>Upload a File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
    # def index():
    #     return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               NEW_FILENAME)


# from app import app
app.run(debug=True, use_debugger=True,
        use_reloader=True)