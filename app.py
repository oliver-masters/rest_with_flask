from src import create_app

# Create an instance of the Flask application using create_app()
app = create_app()

if __name__ == '__main__':
    # Run the Flask application
    app.run()
