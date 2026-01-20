
# Student Record Manager (Python CLI Project)

A command-line **Student Record Management System** built using Python. This project supports full **CRUD operations** (Create, Read, Update, Delete), **JSON-based data storage**, **search functionality**, and **basic analytics** like average age and grade distribution.

This is a strong beginner-to-intermediate project demonstrating practical Python skills such as file handling, structured programming, and real-world application logic.

---

## 🚀 Features

### ✅ Student Management (CRUD)

* Add new student records
* View all stored student records
* Update student details
* Delete student records

### 🔍 Search & Filtering

* Search students by name
* Search students by grade/age (based on project logic)

### 📊 Analytics

* Total number of students
* Average age of students
* Grade distribution summary

### 💾 Data Storage

* Persistent storage using JSON (`student_records.json`)
* Auto load/save records

### 🔐 Backup & Restore

* Create backup of student records
* Restore data from backup file

---

## 🛠 Tech Stack

* **Python 3**
* **JSON** (File storage)
* **CLI (Command Line Interface)**

---

## 📂 Project Structure

```txt
Student-Record-Manager/
│── student_manager.py
│── student_records.json
│── README.md
```

---

## ⚙️ Installation & Setup

### 1) Clone the repository

```bash
git clone https://github.com/Nandd11/Student-Record-Manager.git
cd Student-Record-Manager
```

### 2) Run the program

```bash
python student_manager.py
```

> No external packages required.

---

## 🧪 Demo Output (CLI Preview)

### Main Menu

```txt
=====================================
        STUDENT RECORD MANAGER
=====================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Analytics
7. Backup Records
8. Restore Records
9. Exit
-------------------------------------
Enter your choice:
```

### Add Student

```txt
Enter student name: Nand Patel
Enter age: 20
Enter grade: A
Enter email: nandpatel@gmail.com
Enter phone: 9876543210

✅ Student added successfully!
```

### View Students

```txt
=====================================
          ALL STUDENT RECORDS
=====================================
1) Name: Nand Patel | Age: 20 | Grade: A
   Email: nandpatel@gmail.com | Phone: 9876543210
-------------------------------------
Total Students: 1
```

### Analytics

```txt
=====================================
             ANALYTICS
=====================================
Total Students: 1
Average Age: 20.0

Grade Distribution:
A: 1
B: 0
C: 0
D: 0
```

---

## ✅ Key Learnings

This project helped improve skills in:

* Python fundamentals and problem solving
* File handling and JSON-based persistence
* Building structured CLI applications
* CRUD system design (real-world logic)
* Data analytics using Python

---

## 🔮 Future Improvements

* Add unique Student ID system
* Better input validation (email/phone/age)
* Export records to CSV or Excel
* Add database support (SQLite/MySQL)
* Convert into Web App using Flask / Django

---

## 👤 Author

**Nand Patel**
GitHub: [https://github.com/Nandd11](https://github.com/Nandd11)
