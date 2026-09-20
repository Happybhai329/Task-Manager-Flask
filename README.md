# 📦 Task Manager Flask

A lightweight, session-authenticated Task Management web application built with **Python**, **Flask**, and **Jinja2** templates. It provides a clean and responsive workflow for user onboarding, account management, and real-time task tracking with isolated, user-specific data.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 🌐 Live Demo

Explore the live web application deployed on Render:

🔗 **[https://task-manager-flask-9wr.onrender.com](https://task-manager-flask-9wr.onrender.com)**

---

## 🚀 Features

- **🔐 User Authentication & Session Handling**:
  - Secure registration and login flows with duplicate username detection.
  - Server-side session verification for protected endpoints.
  - One-click logout session clearance.
- **📝 Task Management (CRUD)**:
  - Add new tasks with client-side and server-side validation.
  - Delete completed tasks seamlessly via index-targeted requests.
  - Task isolation ensuring users only see and manage their own tasks.
- **👤 Profile Management**:
  - Dynamic username updates with synchronized data key migration across stored sessions and tasks.
- **💬 Flash Feedback Notifications**:
  - Contextual feedback for registration, invalid credentials, task creation, and account updates.
- **☁️ Production-Ready Cloud Deployment**:
  - Native configuration for Render via `render.yaml` with Gunicorn WSGI server and dynamic port binding.

---

## 🛠️ Tech Stack

| Category | Technology | Description |
|---|---|---|
| **Backend** | [Flask](https://flask.palletsprojects.com/) | Lightweight WSGI micro web framework |
| **Language** | [Python 3](https://www.python.org/) | Core backend programming language |
| **Server** | [Gunicorn](https://gunicorn.org/) | Production WSGI HTTP server |
| **Templating** | [Jinja2](https://jinja.palletsprojects.com/) | Server-side HTML template rendering |
| **Frontend** | HTML5, CSS3 | Clean UI styling and component layout |
| **Deployment** | [Render](https://render.com/) | Cloud platform for automated build & hosting |

---

## 📂 Project Structure

```text
Task-Manager-Flask/
├── static/
│   └── style.css            # Global CSS styling for layouts, forms, buttons, and lists
├── templates/
│   ├── dashboard.html       # Protected user dashboard for task listing and management
│   ├── index.html           # Landing page with conditional navigation based on auth state
│   ├── login.html           # User authentication login form
│   ├── profile.html         # User profile page to modify username
│   └── register.html        # New user registration form
├── .gitignore               # Ignored files, virtual environments, and caches
├── app.py                   # Main Flask application, routing logic, and session control
├── LICENSE                  # MIT License
├── models.py                # Data models for User and Task entities
├── render.yaml              # Infrastructure-as-code deployment blueprint for Render
├── requirements.txt         # Project dependencies (Flask, Gunicorn)
└── README.md                # Project documentation
```

---

## 📋 Prerequisites

Ensure you have the following installed on your local machine:
- **Python 3.8+** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package installer)
- **Git** ([Download Git](https://git-scm.com/))

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Happybhai329/Task-Manager-Flask.git
   cd Task-Manager-Flask
   ```

2. **Create and Activate a Virtual Environment**
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃 Running the Application

### Development Mode
To run the local Flask development server:
```bash
python app.py
```
Open your browser and navigate to:
```text
http://127.0.0.1:5000
```

### Production Mode (Gunicorn)
To run with the production WSGI server:
```bash
gunicorn app:app
```

---

## 🛣️ API & Route Reference

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/` | Public | Landing page with navigation links |
| `GET`, `POST` | `/register` | Public | Register a new user account |
| `GET`, `POST` | `/login` | Public | Authenticate user and initiate session |
| `GET` | `/dashboard` | Protected | Display active user's task list |
| `POST` | `/add_task` | Protected | Add a new task to current user's list |
| `POST` | `/delete_task/<index>` | Protected | Delete a specific task by index |
| `GET`, `POST` | `/profile` | Protected | View and update user profile details |
| `GET` | `/logout` | Protected | Terminate session and redirect to home |

---

## ☁️ Deployment

The repository includes a ready-to-use [`render.yaml`](render.yaml) blueprint for continuous deployment on Render:

```yaml
services:
  - type: web
    name: task-manager-flask
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
```

To deploy your own instance:
1. Push your fork or repository to GitHub.
2. Link your repository in [Render](https://render.com/).
3. Render automatically detects `render.yaml` and executes the build and start commands.

---

## 🔮 Future Roadmap

- [ ] Persistent database layer (SQLite / PostgreSQL with SQLAlchemy)
- [ ] Secure password hashing using `werkzeug.security` (`generate_password_hash`, `check_password_hash`)
- [ ] Task completion checkboxes and priority badges
- [ ] Due dates and reminder notifications
- [ ] Responsive modern CSS framework (Tailwind CSS or Bootstrap)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m "Add some AmazingFeature"`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Happy Bhasin**
- GitHub: [@Happybhai329](https://github.com/Happybhai329)
- Academic: B.Tech CSE (AI Minor)
