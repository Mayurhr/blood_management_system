# 🩸 Blood Management System

A web-based application designed to manage blood donations and requests efficiently. Built using **Flask (Python)** and **MySQL**, this system helps hospitals and individuals to manage donors, handle blood requests, and authenticate users securely.

---

## 🚀 Features

- 🔐 User Authentication with bcrypt
- 🧑‍🤝‍🧑 Donor Registration & Management
- 💉 Blood Request Submission & Tracking
- 🕒 Timestamped entries for all actions

---

## 🧰 Tech Stack

| Layer        | Technology      |
|--------------|-----------------|
| Backend      | Python (Flask)  |
| Frontend     | HTML, CSS       |
| Database     | MySQL           |
| Password Hashing | bcrypt      |

---

## 🗂️ Database Schema

### 🧑 users

| Column        | Type         | Description           |
|---------------|--------------|------------------------|
| id            | int (PK)     | Unique user ID         |
| username      | varchar      | Name of user           |
| email         | varchar      | Email address          |
| phone         | varchar      | Contact number         |
| password      | varchar      | **Hashed password**    |
| registered_on | timestamp    | Time of registration   |

---

### 💉 donors

| Column        | Type         | Description         |
|---------------|--------------|----------------------|
| id            | int (PK)     | Unique donor ID       |
| name          | varchar      | Donor's name          |
| blood_type    | varchar      | Blood group           |
| contact       | varchar      | Contact number        |
| address       | text         | Address               |
| donation_date | timestamp    | Date of donation      |

---

### 🆘 blood_requests

| Column        | Type         | Description          |
|---------------|--------------|-----------------------|
| id            | int (PK)     | Unique request ID     |
| patient_name  | varchar      | Name of the patient   |
| blood_type    | varchar      | Requested blood group |
| contact       | varchar      | Contact number        |
| quantity      | int          | Units required        |
| address       | varchar      | Patient address       |
| request_date  | datetime     | Date of request       |

---

## 🔒 Authentication (bcrypt)

Passwords are stored securely using `bcrypt` hashing.

 ## Install Requirements
 pip install -r requirements.txt

## Setup MySQL
* Import the included blood_management.sql file into your MySQL database.

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'blood_management'


## Project Structure
blood-management-system/
│
├── app.py                  # Main Flask Application
├── templates/              # HTML Templates
|                           # CSS, JS, etc.
├── blood_management.sql    # MySQL Dump File
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation

## Run the Application
> python app.py
