from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost/flask_tasks_db"

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models AFTER initializing db
    from app import models  # This triggers the __init__.py in models/ to load all models

    # Register blueprints
    from app.routes.task_routes import task_bp
    from app.routes.index_routes import index_bp
    app.register_blueprint(task_bp)
    app.register_blueprint(index_bp)

    return app
