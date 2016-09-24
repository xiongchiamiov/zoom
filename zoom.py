#!/usr/bin/env python3

from flask import (
    Flask,
    redirect,
    render_template,
    request,
)
app = Flask(__name__)

redirects = {
    'foo': 'https://duckduckgo.com/',
    'bar': 'https://python.org',
}

@app.route('/create')
def create_new_link():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def handle_new_link():
    link_id = request.form['short-id']
    url = request.form['long-url']

    return 'ok'

@app.route('/<link_id>')
def redirect_to_url(link_id):
    url = redirects[link_id]
    return redirect(url, code=307)
