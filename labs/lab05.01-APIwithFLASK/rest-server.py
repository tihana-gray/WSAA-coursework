# flask server 
# author: Tihana Gray

from flask import Flask, url_for, request, redirect, abort
from bookdao import bookDAO

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"


@app.route('/books', methods=['GET'])
def getall():
    return str(bookDAO.getAll())


@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return str(bookDAO.findByID(id))


@app.route('/books', methods=['POST'])
def create():
    jsonstring = request.json
    return str(bookDAO.create(jsonstring))


@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return str(bookDAO.update(id, jsonstring))


@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return str(bookDAO.delete(id))


if __name__ == "__main__":
    app.run(debug=True)