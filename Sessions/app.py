#!/usr/bin/env3 python3

from flask import Flask, session, request, render_template, url_for, redirect, flash
from os import urandom
import jwt

app = Flask(__name__)
app.secret_key = urandom(24)


@app.route('/', methods=['Get', 'Post'])
def home():
    if request.method == 'POST':
        session.pop('user', None)
        password = request.form['password']
        if password == 'hekmat':
            session['user'] = jwt.encode({'name': 'user'}, app.secret_key)
            return redirect(url_for('protected'))
        if password != 'hekmat':
            flash('You\'ve entered the wrong password!', 'error')
            return redirect(url_for('home'))
    if request.method == 'GET' and 'user' in session:
        return '<h1>Already Logged In</h1>'

    return render_template('index.html')


@app.route('/protected')
def protected():
    try:
        jwt.decode(session['user'], app.secret_key)
        return session['user']
    except:
        return '<h1>You are not authorized</h1>'
    return '<h1>Your are not logged in!</h1>'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return 'Logged out!'


if __name__ == '__main__':
    app.run(debug=True)


# still need to fix everything
# implement SQL database with users and registration
