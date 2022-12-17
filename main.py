from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/show')
def show():
    return render_template('maps.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('index.html')