from flask import Flask, render_template

app = Flask(__name__)
list=["apple", "orange", "banana"]

@app.route('/user/<name>')
def index(name=None):
    return render_template('index.html', name=name, list=list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

app.run(debug=True)