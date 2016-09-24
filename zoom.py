#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/create/')
def hello_world():
    return render_template('create.html')
