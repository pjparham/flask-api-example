from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    page_count = db.Column(db.Integer)
    summary = db.Column(db.String)
    categoy = db.Column(db.String)

    def __repr__(self):
        return f'<Book {self.title} by {self.author} | {self.category} | {self.page_count} pages>'