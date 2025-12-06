# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    tasks = db.relationship("Task", backref="assignee", lazy="dynamic")

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="todo")  # todo | in-progress | done
    priority = db.Column(db.String(50), nullable=False, default="medium")  # low | medium | high
    assignee_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "assignee_id": self.assignee_id,
            "assignee_name": self.assignee.name if self.assignee else None,
        }
