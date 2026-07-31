from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)


with app.app_context():
    db.create_all()


@app.get("/")
def home():
    
    tasks = Task.query.order_by(Task.done.asc(), Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@app.post("/add")
def add():
    title = request.form.get("title", "").strip()
    if not title:
        flash("Task title cannot be empty.", "error")
        return redirect(url_for("home"))

    db.session.add(Task(title=title))
    db.session.commit()
    flash("Task added successfully.", "success")
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
