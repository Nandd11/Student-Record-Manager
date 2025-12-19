"""
Student Record Manager
A Python code to manage student data with full CRUD operations.
"""

import json
import os
from datetime import datetime


class StudentRecordManager:
    """Main class to manage student records"""
    
    def __init__(self, filename="student_records.json"):
        self.filename = filename
        self.students = self.load_records()
    
    def load_records(self):
        """Load student records from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    return json.load(file)
            return {}
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    
    def save_records(self):
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)
    
    def generate_id(self):
        """Generate a unique student ID"""
        if not self.students:
            return "STU001"
        
        # Find the highest ID and increment
        ids = [int(sid[3:]) for sid in self.students.keys() if sid.startswith("STU")]
        if ids:
            new_id = max(ids) + 1
        else:
            new_id = 1
        
        return f"STU{new_id:03d}"
    
    def add_student(self, name, age, grade, email=None, phone=None):
        """For Adding a new student record"""
        student_id = self.generate_id()
        
        student = {
            'id': student_id,
            'name': name,
            'age': age,
            'grade': grade,
            'email': email,
            'phone': phone,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.students[student_id] = student
        self.save_records()
        return student_id
    
    def update_student(self, student_id, **kwargs):
        """Update an existing student record"""
        if student_id not in self.students:
            return False
        
        valid_fields = ['name', 'age', 'grade', 'email', 'phone']
        
        for field, value in kwargs.items():
            if field in valid_fields and value is not None:
                self.students[student_id][field] = value
        
        self.students[student_id]['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_records()
        return True
    
    def delete_student(self, student_id):
        """Delete a student record"""
        if student_id in self.students:
            del self.students[student_id]
            self.save_records()
            return True
        return False
    
    def get_student(self, student_id):
        return self.students.get(student_id, None)
    
    def search_students(self, **criteria):
        """Search students by multiple criteria"""
        results = []
        
        for student in self.students.values():
            match = True
            for key, value in criteria.items():
                if key in student and value:
                    if isinstance(value, str) and value.lower() not in str(student[key]).lower():
                        match = False
                        break
                    elif student[key] != value:
                        match = False
                        break
            
            if match:
                results.append(student)
        
        return results
    
    def get_all_students(self):
        """Get all student records"""
        return list(self.students.values())
    
    def get_statistics(self):
        """Get statistics about student records"""
        if not self.students:
            return {
                'total_students': 0,
                'average_age': 0,
                'grade_distribution': {}
            }
        
        total_students = len(self.students)
        ages = [student['age'] for student in self.students.values()]
        average_age = sum(ages) / total_students
        
        grades = {}
        for student in self.students.values():
            grade = student['grade']
            grades[grade] = grades.get(grade, 0) + 1
        
        return {
            'total_students': total_students,
            'average_age': round(average_age, 2),
            'grade_distribution': grades
        }
    
    def display_student(self, student):
        """For displaying a single student record in a formatted way"""
        print("\n" + "="*50)
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        if student.get('email'):
            print(f"Email: {student['email']}")
        if student.get('phone'):
            print(f"Phone: {student['phone']}")
        print(f"Created: {student['created_at']}")
        print(f"Updated: {student['updated_at']}")
        print("="*50)


class StudentRecordCLI:
    def __init__(self):
        self.manager = StudentRecordManager()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """for displaying the main menu"""
        print("\n" + "="*60)
        print("STUDENT RECORD MANAGER".center(60))
        print("="*60)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Statistics")
        print("7. Backup Records")
        print("8. Restore Records")
        print("9. Exit")
        print("="*60)
    
    def get_valid_input(self, prompt, validation_func=None, error_msg="Invalid input"):
        """Get valid input from user"""
        while True:
            try:
                value = input(prompt).strip()
                if validation_func:
                    value = validation_func(value)
                return value
            except ValueError:
                print(f"Error: {error_msg}")
    
    def validate_age(self, age_str):
        age = int(age_str)
        if not 5 <= age <= 100:
            raise ValueError("Age must be between 5 and 100")
        return age
    
    def validate_grade(self, grade_str):
        grade = grade_str.upper()
        if grade not in ['A', 'B', 'C', 'D', 'F']:
            raise ValueError("Grade must be A, B, C, D, or F")
        return grade
    
    def add_student_ui(self):
        """ For adding a student"""
        print("\n--- ADD NEW STUDENT ---")
        
        name = self.get_valid_input("Enter student name: ", 
                                   lambda x: x if x else ValueError("Name cannot be empty"))
        
        age = self.get_valid_input("Enter student age (5-100): ", 
                                  self.validate_age, "Age must be a number between 5-100")
        
        grade = self.get_valid_input("Enter grade (A, B, C, D, F): ", 
                                    self.validate_grade, "Invalid grade")
        
        email = input("Enter email (optional): ").strip() or None
        phone = input("Enter phone number (optional): ").strip() or None
        
        student_id = self.manager.add_student(name, age, grade, email, phone)
        print(f"\n✓ Student added successfully! Student ID: {student_id}")
    
    def view_all_students_ui(self):
        students = self.manager.get_all_students()
        
        if not students:
            print("\nNo student records found.")
            return
        
        print(f"\n--- ALL STUDENTS ({len(students)} records) ---")
        
        # Sort students by name
        students.sort(key=lambda x: x['name'])
        
        for student in students:
            self.manager.display_student(student)
        
        input("\nPress Enter to continue...")
    
    def search_students_ui(self):
        print("\n--- SEARCH STUDENTS ---")
        print("Enter search criteria (leave blank to skip):")
        
        name = input("Name: ").strip() or None
        age_str = input("Age: ").strip()
        age = int(age_str) if age_str.isdigit() else None
        grade = input("Grade (A, B, C, D, F): ").strip().upper() or None
        grade = grade if grade in ['A', 'B', 'C', 'D', 'F', ''] else None
        
        results = self.manager.search_students(name=name, age=age, grade=grade)
        
        if results:
            print(f"\n✓ Found {len(results)} matching student(s):")
            for student in results:
                self.manager.display_student(student)
        else:
            print("\n✗ No students found matching the criteria.")
        
        input("\nPress Enter to continue...")
    
    def update_student_ui(self):
        print("\n--- UPDATE STUDENT ---")
        
        student_id = input("Enter student ID to update: ").strip().upper()
        
        student = self.manager.get_student(student_id)
        if not student:
            print(f"\n✗ Student with ID {student_id} not found.")
            return
        
        print("\nCurrent student details:")
        self.manager.display_student(student)
        
        print("\nEnter new values (leave blank to keep current):")
        
        name = input(f"Name [{student['name']}]: ").strip()
        name = name if name else None
        
        age_str = input(f"Age [{student['age']}]: ").strip()
        age = int(age_str) if age_str.isdigit() else None
        
        grade = input(f"Grade [{student['grade']}]: ").strip().upper()
        grade = grade if grade in ['A', 'B', 'C', 'D', 'F', ''] else None
        
        email = input(f"Email [{student.get('email', 'None')}]: ").strip()
        email = email if email else None
        
        phone = input(f"Phone [{student.get('phone', 'None')}]: ").strip()
        phone = phone if phone else None
        
        if self.manager.update_student(
            student_id, 
            name=name, 
            age=age, 
            grade=grade, 
            email=email, 
            phone=phone
        ):
            print(f"\n✓ Student {student_id} updated successfully!")
        else:
            print(f"\n✗ Failed to update student {student_id}.")
    
    def delete_student_ui(self):

        print("\n--- DELETE STUDENT ---")
        
        student_id = input("Enter student ID to delete: ").strip().upper()
        
        student = self.manager.get_student(student_id)
        if not student:
            print(f"\n✗ Student with ID {student_id} not found.")
            return
        
        print("\nStudent to delete:")
        self.manager.display_student(student)
        
        confirm = input(f"\nAre you sure you want to delete {student['name']}? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            if self.manager.delete_student(student_id):
                print(f"\n✓ Student {student_id} deleted successfully!")
            else:
                print(f"\n✗ Failed to delete student {student_id}.")
        else:
            print("\nDeletion cancelled.")
    
    def view_statistics_ui(self):
        """User interface for viewing statistics"""
        stats = self.manager.get_statistics()
        
        print("\n--- STATISTICS ---")
        print(f"Total Students: {stats['total_students']}")
        print(f"Average Age: {stats['average_age']}")
        
        print("\nGrade Distribution:")
        for grade, count in stats['grade_distribution'].items():
            print(f"  {grade}: {count} student(s)")
        
        input("\nPress Enter to continue...")
    
    def backup_records_ui(self):
        """Create a backup of student records"""
        backup_file = f"student_records_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(backup_file, 'w') as file:
                json.dump(self.manager.students, file, indent=4)
            print(f"\n✓ Backup created successfully: {backup_file}")
        except Exception as e:
            print(f"\n✗ Failed to create backup: {e}")
    
    def restore_records_ui(self):
        """Restore student records from backup"""
        backup_files = [f for f in os.listdir('.') if f.startswith('student_records_backup')]
        
        if not backup_files:
            print("\n✗ No backup files found.")
            return
        
        print("\nAvailable backup files:")
        for i, file in enumerate(sorted(backup_files, reverse=True), 1):
            print(f"{i}. {file}")
        
        try:
            choice = int(input("\nSelect backup to restore (number): "))
            if 1 <= choice <= len(backup_files):
                backup_file = backup_files[choice - 1]
                
                with open(backup_file, 'r') as file:
                    backup_data = json.load(file)
                
                self.manager.students = backup_data
                self.manager.save_records()
                print(f"\n✓ Records restored from {backup_file}")
            else:
                print("\n✗ Invalid selection.")
        except (ValueError, json.JSONDecodeError) as e:
            print(f"\n✗ Failed to restore: {e}")
    
    def run(self):
        
        self.clear_screen()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-9): ").strip()
                
                if choice == '1':
                    self.add_student_ui()
                elif choice == '2':
                    self.view_all_students_ui()
                elif choice == '3':
                    self.search_students_ui()
                elif choice == '4':
                    self.update_student_ui()
                elif choice == '5':
                    self.delete_student_ui()
                elif choice == '6':
                    self.view_statistics_ui()
                elif choice == '7':
                    self.backup_records_ui()
                elif choice == '8':
                    self.restore_records_ui()
                elif choice == '9':
                    print("\nThank you for using Student Record Manager. Goodbye!")
                    break
                else:
                    print("\n✗ Invalid choice. Please enter a number between 1-9.")
                
                input("\nPress Enter to continue...")
                self.clear_screen()
                
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n✗ An error occurred: {e}")
                input("Press Enter to continue...")


if __name__ == "__main__":
    app = StudentRecordCLI()
    app.run()