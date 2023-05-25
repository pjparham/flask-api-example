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
    
    def post(self):
        data = request.get_json()

        new_book = Book(
            title=data['title'],
            author=data['author'],
            page_count=data['page_count'],
            summary=data['summary'],
            category=data['category']
        )

        db.session.add(new_book)
        db.session.commit()
        
        return make_response(new_book.to_dict(), 201)

    
api.add_resource(Books, '/books')

class BookByID(Resource):

    def get(self, id):
        book = Book.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(book), 200)
    
    def patch(self, id):
        data = request.get_json()
        book = Book.query.filter_by(id=id).first()
        for attr in data:
            setattr(book, attr, data[attr])

        db.session.add(book)
        db.session.commit()

        response_dict = book.to_dict()
        return make_response(response_dict, 200)
    
    def delete(self, id) :
        book = Book.query.filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "Book deleted."
        }

        response = make_response(
            response_body,
            200
        )

        return response
    
api.add_resource(BookByID, '/books/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)