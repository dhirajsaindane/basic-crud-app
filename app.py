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

    # Import models
    from models import Department, Employee

    # Register routes
    from routes import main
    app.register_blueprint(main)

    return app

# ---------- VERY IMPORTANT FOR VERCEL ----------
app = create_app()   # app is the Flask instance
handler = app        # handler must be the same Flask instance
# ------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
