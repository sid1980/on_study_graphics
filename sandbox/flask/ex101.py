# coding: utf-8
# TeamTreeHouse
# TeamTreeHouse - Flask Basics[TeamTreeHouse-Exclusive]

from flask import Flask
# from flask import request

app = Flask(__name__)

# first variant
'''
from flask import request
@app.route('/')
def index(name="test"):
    name = request.args.get('name', name)
    return "hello {}".format(name)
'''

# second variant
@app.route('/')
@app.route('/<name>')
def index(name="test"):
    return "hello {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)
    return '{}+{}={}'.format(num1, num2, num1+num2)


app.run(debug=True, port=8000, host='0.0.0.0')
