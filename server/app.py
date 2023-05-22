from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Resource, Api

from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Books(Resource):
    def get(self):
        books = [book.to_dict() for book in Book.query.all()]
        return make_response(jsonify(books), 200)
    
api.add_resource(Books, '/books')
if __name__ == '__main__':
    app.run(port=5555, debug=True)