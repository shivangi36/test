from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    published_date = db.Column(db.Date, nullable=False)

    def __init__(self, title, author, isbn, published_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_date = published_date

    def __repr__(self):
        return f'<Book {self.title}>'
