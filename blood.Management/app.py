from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import bcrypt  # Added bcrypt

app = Flask(__name__)
app.secret_key = 'mayurhr@127'  # Replace with a secure key

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mayur@127'
app.config['MYSQL_DB'] = 'blood_management'

mysql = MySQL(app)

# Route for the login page
@app.route('/')
def login_page():
    return render_template('login.html')

# Login endpoint with bcrypt password check
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        flash('Login successful!', 'success')
        return redirect(url_for('blood_page'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('login_page'))

# Register endpoint with bcrypt password hashing
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')

    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO users (username, email, phone, password)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (username, email, phone, hashed_password))
    mysql.connection.commit()
    cursor.close()

    flash('Registration successful! Please log in.', 'success')
    return redirect(url_for('login_page'))

# Route for the blood donation connect page
@app.route('/blood')
def blood_page():
    return render_template('blood.html')

# Donor registration
@app.route('/add_donor', methods=['POST'])
def add_donor():
    name = request.form.get('name')
    blood_type = request.form.get('blood_type')
    contact = request.form.get('contact')
    address = request.form.get('address')
    
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO donors (name, blood_type, contact, address)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, blood_type, contact, address))
    mysql.connection.commit()
    cursor.close()
    
    flash('Donor registered successfully!', 'success')
    return redirect(url_for('blood_page'))

# Blood request submission
@app.route('/add_request', methods=['POST'])
def add_request():
    req_name = request.form.get('req_name')
    req_blood_type = request.form.get('req_blood_type')
    req_contact = request.form.get('req_contact')
    quantity = request.form.get('quantity')
    address = request.form.get('address')
    
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO blood_requests (patient_name, blood_type, contact, quantity, address)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (req_name, req_blood_type, req_contact, quantity, address))
    mysql.connection.commit()
    cursor.close()
    
    flash('Blood request submitted successfully!', 'success')
    return redirect(url_for('blood_page'))

if __name__ == "__main__":
    app.run(debug=True)