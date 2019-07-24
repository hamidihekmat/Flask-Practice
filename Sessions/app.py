#!/usr/bin/env3 python3

from flask import Flask, session, request, render_template, url_for, redirect


app = Flask(__name__)
app.secret_key = b'_53y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['Get', 'Post'])
def home():
    if request.method == 'POST':
        session.pop('user', None)
        password = request.form['password']
        if password == 'hekmat':
            session['user'] = 'hekmat'
            return redirect(url_for('protected'))
    if request.method == 'GET' and 'user' in session:
        return '<h1>Already Logged In</h1>'

    return render_template('index.html')


@app.route('/protected')
def protected():
    if 'user' in session:
        return session['user']
    return 'Your are not logged in!'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return 'Logged out!'


if __name__ == '__main__':
    app.run(debug=True)


# still need to fix everything
