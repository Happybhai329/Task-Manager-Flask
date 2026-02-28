from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import User, Task

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# In-memory storage
users = {}
tasks = {}

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists!', 'danger')
        else:
            users[username] = User(username, password)
            tasks[username] = []
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username].password == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'danger')

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    user_tasks = tasks.get(session['username'], [])
    return render_template('dashboard.html', tasks=user_tasks)

# Add Task
@app.route('/add_task', methods=['POST'])
def add_task():
    if 'username' in session:
        content = request.form['task']

        if content.strip():
            tasks[session['username']].append(Task(content))
            flash('Task added!', 'success')
        else:
            flash('Task cannot be empty!', 'danger')

    return redirect(url_for('dashboard'))

# Delete Task
@app.route('/delete_task/<int:index>', methods=['POST'])
def delete_task(index):
    if 'username' in session:
        user_tasks = tasks.get(session['username'], [])

        if 0 <= index < len(user_tasks):
            del user_tasks[index]
            flash('Task deleted!', 'success')

    return redirect(url_for('dashboard'))

# Profile Route (FIXED)
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = users[session['username']]

    if request.method == 'POST':
        new_username = request.form['username']

        if new_username and new_username != session['username']:
            users[new_username] = users.pop(session['username'])
            tasks[new_username] = tasks.pop(session['username'])
            session['username'] = new_username
            flash('Profile updated!', 'success')
            return redirect(url_for('profile'))

    return render_template('profile.html', user=user)

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)