from flask import Flask
from dotenv import load_dotenv
import os
from extensions import db

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = "234fvgw#$"

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from models import Department, Employee
    from routes import main
    app.register_blueprint(main)

    return app


app = create_app()
handler = app  # for Vercel

if __name__ == "__main__":
    app.run(debug=True)
