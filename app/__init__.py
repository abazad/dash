from flask import Flask
app = Flask(__name__)
app.secret_key = 'kevmo'
from app import views