from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost/flask_tasks"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost/flask_tasks_db"
app.config["SECRET_KEY"] = "dev" #mcm laravel php artisan generate key
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") kalau define kat env

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# from app import routes  # Make sure routes are registered
from app import routes, models