# 📝 Task Tracking Application (Python Full Stack)     

A full-stack **Task Tracking Web Application** built using **Python Flask**, **SQLite**, and **Vanilla JavaScript**.
This app allows users to create, assign, update, delete, and track tasks with real-time statistics using derived selectors.

---

## 🚀 Features     

* Create and manage users
* Create, assign, update, and delete tasks  
* Task status tracking (To-Do, In-Progress, Done)
* Task priority support 
* User–Task relationship (one user → many tasks)
* Search and filter tasks
* Derived selectors:

  * Task count by status
  * Open task count
  * Tasks by user
* Clean UI with real-time updates

---

## 🛠 Tech Stack

### Backend

* Python 3.11
* Flask
* Flask-SQLAlchemy
* Flask-CORS
* SQLite

### Frontend

* HTML
* CSS
* JavaScript (Vanilla)

---

## 📁 Project Structure

```
TaskTracking/
├── app.py
├── models.py
├── requirements.txt
├── static/
│   ├── app.js
│   └── styles.css
├── templates/
│   └── index.html
└── .venv/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/DevuDhanu/task-tracking-application.git
cd task-tracking-app
```

---

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

---

### 3️⃣ Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

If blocked, run once:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows (CMD):**

```cmd
.\.venv\Scripts\activate.bat
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the application

```bash
python app.py
```

---

### 6️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🧪 How to Use the App

### 👤 Users

* Add users from the **Users** section
* Click on a user name to view their assigned tasks

### ✅ Tasks

* Create tasks with title, priority, and assignee
* Update task status using dropdown
* Reassign tasks to different users
* Delete tasks when completed

### 📊 Selectors / Stats

* View total tasks by status
* See open task count
* Filter tasks by user or status

---

## 📦 Requirements File

`requirements.txt`

```
Flask==2.2.5
Flask-SQLAlchemy==3.0.3
Flask-Cors==3.0.10
```

This ensures consistent dependency installation across systems.

---

## 🎯 Learning Outcomes

* Python Flask full-stack development
* REST API design
* Database relationships (One-to-Many)
* Frontend–Backend integration
* Use of derived state (selectors)
* Project structuring and GitHub workflow

---

## 📌 Future Improvements

* User authentication (Login/Signup)
* Role-based access
* React frontend
* REST API documentation (Swagger)
* Cloud deployment (Render / AWS)

---

## 👨‍💻 Author

**Dhanu**
Python | Flask | Full-Stack Development


Just say the word.
