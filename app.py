from flask import Flask, render_template

app = Flask(__name__)
list=["apple", "orange", "banana"]

@app.route('/user/<name>')
def index(name=None):
    return render_template('index.html', name=name, list=list)


app.run(debug=True)