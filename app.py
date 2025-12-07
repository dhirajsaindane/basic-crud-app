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

    with app.app_context():
        db.create_all()

    from routes import main
    app.register_blueprint(main)

    return app

# 👉 ADD THIS FOR VERCEL
app = create_app()
handler = app  # optional but recommended for Vercel

if __name__ == "__main__":
    app.run(debug=True)
