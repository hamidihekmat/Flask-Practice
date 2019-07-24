#!/usr/bin/env python3

import pyrebase

config = {
    "apiKey": "AIzaSyCrsmE2GjJRA0OmijMastQ5fUuH8EAu5pc",
    "authDomain": "innate-star-228407.firebaseapp.com",
    "databaseURL": "https://innate-star-228407.firebaseio.com",
    "projectId": "innate-star-228407",
    "storageBucket": "innate-star-228407.appspot.com",
    "messagingSenderId": "130872333529",
    "appId": "1:130872333529:web:1fdab67c0dff6a99"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#https://www.youtube.com/watch?v=aojoWWMN1r0

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        db.child('todo').push(name)
        todo = db.child('todo').get()
        to = todo.val()
        print(todo)
        return render_template('index.html', t=to.values())
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
