from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'this is a secret'

@app.route('/')
def index():
    flash('Welcome to my website guest!')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
