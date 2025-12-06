# app.py
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from models import db, User, Task
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "db.sqlite")

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
CORS(app)

# --- DB init / seed helper ---
def init_db(app):
    with app.app_context():
        db.create_all()
        # seed if empty
        if User.query.count() == 0:
            u1 = User(name="Alice")
            u2 = User(name="Bob")
            u3 = User(name="Charlie")
            db.session.add_all([u1, u2, u3])
            db.session.commit()
        if Task.query.count() == 0:
            t1 = Task(title="Design landing page", status="todo", priority="high", assignee_id=1)
            t2 = Task(title="API: auth endpoints", status="in-progress", priority="medium", assignee_id=2)
            t3 = Task(title="Write tests", status="done", priority="low")
            db.session.add_all([t1, t2, t3])
            db.session.commit()

# --- Routes for serving frontend ---
@app.route("/")
def index():
    return render_template("index.html")

# --- API: Users ---
@app.route("/api/users", methods=["GET"])
def list_users():
    users = [u.to_dict() for u in User.query.order_by(User.id).all()]
    return jsonify(users), 200

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    if not name:
        return jsonify({"error": "name is required"}), 400
    if User.query.filter_by(name=name).first():
        return jsonify({"error": "user already exists"}), 400
    u = User(name=name)
    db.session.add(u)
    db.session.commit()
    return jsonify(u.to_dict()), 201

@app.route("/api/users/<int:user_id>/tasks", methods=["GET"])
def tasks_by_user(user_id):
    user = User.query.get_or_404(user_id)
    tasks = [t.to_dict() for t in user.tasks.order_by(Task.id).all()]
    return jsonify(tasks), 200

# --- API: Tasks ---
@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    tasks = [t.to_dict() for t in Task.query.order_by(Task.id).all()]
    return jsonify(tasks), 200

@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json() or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title required"}), 400
    priority = data.get("priority", "medium")
    assignee_id = data.get("assignee_id")
    if assignee_id:
        if not User.query.get(assignee_id):
            return jsonify({"error": "assignee_id invalid"}), 400
    t = Task(title=title, priority=priority, assignee_id=assignee_id)
    db.session.add(t)
    db.session.commit()
    return jsonify(t.to_dict()), 201

@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    t = Task.query.get_or_404(task_id)
    data = request.get_json() or {}
    # allowed fields: title, status, priority, assignee_id
    if "title" in data:
        t.title = data["title"].strip() or t.title
    if "status" in data:
        if data["status"] not in ("todo", "in-progress", "done"):
            return jsonify({"error": "invalid status"}), 400
        t.status = data["status"]
    if "priority" in data:
        t.priority = data["priority"]
    if "assignee_id" in data:
        aid = data["assignee_id"]
        if aid is not None and not User.query.get(aid):
            return jsonify({"error": "assignee_id invalid"}), 400
        t.assignee_id = aid
    db.session.commit()
    return jsonify(t.to_dict()), 200

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    t = Task.query.get_or_404(task_id)
    db.session.delete(t)
    db.session.commit()
    return jsonify({"ok": True}), 200

# --- Derived selector endpoints ---
@app.route("/api/tasks/counts_by_status", methods=["GET"])
def counts_by_status():
    counts = {"todo": 0, "in-progress": 0, "done": 0}
    for t in Task.query.all():
        counts[t.status] = counts.get(t.status, 0) + 1
    return jsonify(counts), 200

@app.route("/api/tasks/open_count", methods=["GET"])
def open_count():
    c = Task.query.filter(Task.status != "done").count()
    return jsonify({"open": c}), 200

# --- bootstrap ---
if __name__ == "__main__":
    init_db(app)
    app.run(debug=True, host="127.0.0.1", port=5000)
