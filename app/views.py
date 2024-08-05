from flask import render_template, request
from app import app
from app.controllers import produtos, usuarios

@app.route('/')
def home():
    return render_template('index.html', produtos=produtos)