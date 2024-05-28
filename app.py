# app.py

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define database models (User, Data, AdditionalTable) and their relationships
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Hashed password for security

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add fields based on data requirements

class AdditionalTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add fields based on additional table requirements

if __name__ == '__main__':
    app.run(debug=True)from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define database models (User, Data, AdditionalTable) and their relationships here

if __name__ == '__main__':
    app.run(debug=True)

# Import necessary modules for user authentication
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# Define User model and load_user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registration route and form handling
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!', 'error')
            return redirect(url_for('register'))

        # Create a new user and hash the password
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login route and form handling
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route for displaying data on the user page
@app.route('/')
def user_page():
    # Fetch data from the database (e.g., Data model)
    data = Data.query.all()
    return render_template('user_page.html', data=data)

# Route for displaying data on the admin page
@app.route('/admin')
@login_required  # Require authentication to access admin page
def admin_page():
    # Fetch data from the database (e.g., Data model)
    data = Data.query.all()
    return render_template('admin_page.html', data=data)

# Detail page route for a specific data item
@app.route('/data/<int:data_id>')
def data_detail(data_id):
    # Fetch a specific data item from the database
    data_item = Data.query.get_or_404(data_id)
    return render_template('data_detail.html', data=data_item)

# Route for inserting data through the admin page
@app.route('/insert', methods=['POST'])
@login_required  
def insert_data():
    # Process form data and insert into the database (Data model)
    # Insert logic here
    flash('Data inserted successfully!', 'success')
    return redirect(url_for('admin_page'))

# Route for updating data through the admin page
@app.route('/update/<int:data_id>', methods=['POST'])
@login_required  
def update_data(data_id):
    data_item = Data.query.get_or_404(data_id)
    
    # Process form data and update the data in the database
    # Update logic here
    flash('Data updated successfully!', 'success')
    return redirect(url_for('admin_page'))

# Route for deleting data through the admin page
@app.route('/delete/<int:data_id>', methods=['POST'])
@login_required  
def delete_data(data_id):
    data_item = Data.query.get_or_404(data_id)
    
    # Delete the data from the database
    db.session.delete(data_item)
    db.session.commit()
    flash('Data deleted successfully!', 'success')
    return redirect(url_for('admin_page'))

# AJAX search route for searching data
@app.route('/search', methods=['POST'])
@login_required  
def search_data():
    search_term = request.form['search_term']
    
    # Perform search in the database based on the search term
    # Search logic here
    # Return search results as JSON response
    return jsonify(search_results)

# Import necessary libraries for PDF generation and sorting
from reportlab.pdfgen import canvas
from sqlalchemy.orm import relationship

# Define the relationships between tables
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    data = db.relationship('Data', backref='user', lazy=True)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add fields with relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Data sorting route based on categories
@app.route('/sort/<category>')
@login_required
def sort_data(category):
    if category == 'name':
        sorted_data = Data.query.order_by(Data.name).all()
    elif category == 'email':
        sorted_data = Data.query.order_by(Data.email).all()
    elif category == 'university':
        sorted_data = Data.query.order_by(Data.university).all()
    else:
        # Handle sorting for other categories
    
    return render_template('sorted_data.html', data=sorted_data)

# PDF report generation route
@app.route('/report/pdf')
@login_required
def generate_report():
    # Generate PDF report using ReportLab library
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=report.pdf'

    c = canvas.Canvas('report.pdf')
    c.drawString(100, 750, "PDF Report")
    # Add content to the PDF report
    c.showPage()
    c.save()

    return send_file('report.pdf')

if __name__ == '__main__':
    app.run(debug=True)