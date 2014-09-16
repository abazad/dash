import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

app = Flask(__name__)

# from app import views