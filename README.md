# 🎓 Student Management System

A Django-based Student Management System designed to manage students, teachers, classes, subjects, attendance, marks, and report cards through role-based access.

## 🌐 Live Demo

**Live Application:** https://alirazadev.pythonanywhere.com/

## 🚀 Features

### 👨‍💼 Admin

* Manage students
* Manage teachers
* Manage classes
* Manage subjects
* Manage attendance
* Manage marks
* View report cards
* Role-based permissions

### 👨‍🏫 Teacher

* Teacher dashboard
* View students
* View classes
* View subjects
* Record attendance
* Update attendance according to permissions
* Add marks
* Update marks according to permissions
* View report cards

### 🎓 Student

* Student dashboard
* View personal information
* View marks
* View attendance
* View report card

### 👨‍👩‍👧 Parent

* Parent dashboard
* View child's attendance
* View child's marks
* View child's report card

## 📊 Academic Management

The system supports:

* Multiple classes and sections
* Subjects assigned to classes and teachers
* Student attendance records
* Mid-Term and Final-Term marks
* Report cards
* Student-parent relationships

## 🔐 Authentication & Permissions

The project uses Django authentication and group-based permissions to control what different users can access.

The main roles are:

```text
Admin
 ├── Full system management

Teacher
 ├── Students
 ├── Classes
 ├── Attendance
 └── Marks

Student
 └── Own academic information

Parent
 └── Child's academic information
```

## 🛠️ Technology Stack

* Python
* Django
* SQLite
* HTML
* CSS
* Bootstrap
* Git
* GitHub
* PythonAnywhere

## 🗂️ Main Models

The application uses Django models for:

* SchoolClass
* Students
* Teachers
* Subjects
* Attendence
* Marks
* Parents

These models are connected through relationships to manage the academic data.

## 📸 Project

The application includes separate dashboards and interfaces for different user roles.

The live version is populated with realistic demo data so the system can be explored without using private information.

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/Ali-Raza21X/Student-Management-System.git
```

Enter the project directory:

```bash
cd Student-Management-System
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 📌 Project Status

**Version 1 — Completed and Deployed**

The first version of the system has been completed, tested with multiple user roles, populated with demo data, and deployed on PythonAnywhere.

## 🔗 Links

🌐 **Live Demo:** https://alirazadev.pythonanywhere.com/

💻 **GitHub:** https://github.com/Ali-Raza21X/Student-Management-System

👤 **Developer:** Ali Raza
