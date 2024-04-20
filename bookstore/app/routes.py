from flask import Blueprint, request, jsonify
from .models import Book, db
from datetime import datetime

# Create a blueprint for routes
bp = Blueprint('main', __name__)

# Endpoint to add a new book
@bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title=data['title'],
        author=data['author'],
        isbn=data['isbn'],
        published_date=datetime.strptime(data['published_date'], '%Y-%m-%d')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

# Endpoint to list all books
@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'published_date': book.published_date.strftime('%Y-%m-%d')
        }
        output.append(book_data)
    return jsonify({'books': output})

# Endpoint to retrieve a book by ISBN
@bp.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    book_data = {
        'title': book.title,
        'author': book.author,
        'isbn': book.isbn,
        'published_date': book.published_date.strftime('%Y-%m-%d')
    }
    return jsonify({'book': book_data})

# Endpoint to update a book's details
@bp.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    data = request.json
    book.title = data['title']
    book.author = data['author']
    book.published_date = datetime.strptime(data['published_date'], '%Y-%m-%d')
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

# Endpoint to delete a book
@bp.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})
