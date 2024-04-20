from flask import Flask
from .models import db

# Create the Flask application
def create_app():
    app = Flask(__name__)

    # Configuration for SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Import and register routes blueprint
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
