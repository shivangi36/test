from app import create_app

# Create the Flask application instance
if __name__ == '__main__':
    # Create the Flask app using the create_app function defined in __init__.py
    app = create_app()
    
    # Run the Flask app in debug mode
    app.run(debug=True)
