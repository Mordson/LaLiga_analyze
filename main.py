from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/show')
def show():
    return render_template('maps.html')