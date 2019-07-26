#!/usr/bin/env3 python3

from flask import Flask, session, request, render_template, url_for, redirect, flash
from os import urandom
import jwt
import datetime

app = Flask(__name__)
app.secret_key = urandom(24)


@app.route('/', methods=['Get', 'Post'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'hekmat':
            session['user'] = jwt.encode({'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(seconds=30)}, app.secret_key)
            return redirect(url_for('protected'))
        if password != 'hekmat':
            flash('You\'ve entered the wrong password!', 'error')
            return redirect(url_for('home'))
    if request.method == 'GET':
        try:
            jwt.decode(session['user'], app.secret_key)
            return redirect(url_for('protected'))
        except:
            return render_template('index.html')
    return render_template('index.html')


@app.route('/protected')
def protected():
    try:
        jwt.decode(session['user'], app.secret_key)
        return session['user']
    except:
        return '<h1>You are not authorized</h1>', 403
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return 'Logged out!'


if __name__ == '__main__':
    app.run(debug=True)


# still need to fix everything
# implement SQL database with users and registration
