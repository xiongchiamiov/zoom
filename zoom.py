#!/usr/bin/env python3

from flask import (
    Flask,
    render_template,
    request,
)
app = Flask(__name__)

@app.route('/create')
def create_new_link():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def handle_new_link():
    link_id = request.form['short-id']
    url = request.form['long-url']

    return 'ok'
