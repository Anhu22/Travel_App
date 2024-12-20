# app/routes.py

from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def valid_user(username, password):
    # Replace this with your actual user validation logic
    return username == "admin" and password == "password"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Validate username and password
    if valid_user(username, password):
        session['user'] = username  # Store user in session
        return redirect(url_for('homepage'))
    return 'Invalid credentials', 403

@app.route('/homepage')
def homepage():
    if 'user' not in session:  # Check if user is authenticated
        return redirect(url_for('login_page'))  # Redirect to login if not authenticated
    return 'Welcome to the homepage!'

@app.route('/login_page')
def login_page():
    return render_template('login.html')  # Render the login HTML template

if __name__ == '__main__':
    app.run()