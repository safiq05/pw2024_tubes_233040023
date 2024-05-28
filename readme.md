# Flask Web Application Project Documentation
Flask web application project that includes user authentication, data management, PDF reporting, sorting functionalities, and more.

Proyek aplikasi web Flask yang mencakup otentikasi pengguna, manajemen data, pelaporan PDF, fungsi pengurutan, dan banyak lagi.

## Features
- User Registration and Login
- User and Admin Pages
- CRUD Operations: Insert, Update, Delete Data
- Data Sorting by Categories
- PDF Reporting
- AJAX Search Functionality
- Database Models and Relationships
- Flask-Migrate for Database Migrations
- RESTful API Endpoints

## Technologies Used
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Migrate
- ReportLab for PDF Generation

## Installation and Setup
1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up the database by running migrations with `flask db migrate` and `flask db upgrade`.
5. Set the Flask app name: `export FLASK_APP=app.py`.
6. Run the Flask application using `flask run`.

## Project Structure
- `app.py`: Main application file containing routes and configurations.
- `templates/`: HTML templates for the web pages.
- `static/`: Static files (CSS, JavaScript, images).
- `migrations/`: Database migration scripts.
- `requirements.txt`: List of project dependencies.
- `.flaskenv`: Environment variables configuration.
- `.gitignore`: Files and directories to be ignored by Git.

## Usage
- Register a new user or login with existing credentials.
- Access user or admin pages based on authentication.
- Perform CRUD operations on data through the admin page.
- Generate PDF reports and search data using the web application.
- Sort data based on categories like name, email, university.

## Contribution
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/add-new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/add-new-feature`).
5. Create a new Pull Request.
