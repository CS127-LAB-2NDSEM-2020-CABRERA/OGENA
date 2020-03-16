import logging

from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("Ogena_Portfolio.html")

if __name__ == '__main__':
    app.run(debug=True)