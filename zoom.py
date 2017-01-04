#!/usr/bin/env python3

# May you recognize your weaknesses and share your strengths.
# May you share freely, never taking more than you give.
# May you find love and love everyone you find.

import os
import sqlite3

from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
)
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db_path = os.path.join(app.instance_path, 'zoom.db')
        db = sqlite3.connect(db_path)
        db.row_factory = sqlite3.Row
        g._database = db

    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Initialize the database.

    Use this like so:
        >>> from zoom import init_db
        >>> init_db()
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/create')
def create_new_link():
    redirects = query_db('select * from redirects')
    return render_template('create.html', redirects=redirects)

@app.route('/create', methods=['POST'])
def handle_new_link():
    link_id = request.form['short-id']
    url = request.form['long-url']
    try:
        db = get_db()
        db.execute('insert into redirects values (?, ?)', (link_id, url))
        db.commit()
    except sqlite3.IntegrityError:
        return 'sorry, key already used'

    return 'ok'

@app.route('/<link_id>')
def redirect_to_url(link_id):
    row = query_db('select url from redirects where id=?', (link_id,), one=True)
    if not row:
        return 'not found'
    return redirect(row['url'], code=307)
