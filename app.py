from flask import Flask, render_template, request, redirect, url_for  
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os
# Create a Flask application instances
app = Flask(__name__)
# Configure the application
app.config['SECRET_KEY'] = "the-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize the database
db = SQLAlchemy(app)
# Define a model for the tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    done = db.Column(db.Boolean,default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)




with app.app_context():
    if not os.path.exists('todo.db'):
        db.create_all()


# Define a route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
