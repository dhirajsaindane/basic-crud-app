from flask import Flask
from dotenv import load_dotenv
import os
from extensions import db   # <-- correct place to import db

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = "234fvgw#$"

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db
    db.init_app(app)

    # Import models AFTER init_app
    from models import Department, Employee

    # Create tables
    with app.app_context():
        db.create_all()

    # Register blueprint AFTER db + models configured
    from routes import main
    app.register_blueprint(main)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
