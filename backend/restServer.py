from crypt import methods
from flask import Flask, render_template, request
import siteDB as dbClient
import json

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('home.html')


#*   handle user dir   *#
@app.route('/user', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def userDir():
    pass

@app.route('/user/id', methods = ['GET', 'PUT', 'DELETE'])
def userDir():
    pass

#*   handle tickets dir   *#
@app.route('/tickets', methods = ['GET', 'POST', 'DELETE'])
def userDir():
    pass

@app.route('/tickets/id', methods = ['GET', 'DELETE'])
def userDir():
    pass


#*   handle flights dir   *#
@app.route('/flights', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def userDir():
    pass

@app.route('/flights/id', methods = ['GET', 'PUT', 'DELETE'])
def userDir():
    pass


#*   handle countries dir   *#
@app.route('/countries', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def userDir():
    pass

@app.route('/countries/id', methods = ['GET', 'PUT', 'DELETE'])
def userDir():
    pass


if __name__ == '__main__':
    app.run(debug = True)