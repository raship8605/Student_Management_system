class Student:
    all_students = []

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    # Update marks
    def update_marks(self, new_marks):
        self.marks = new_marks

    # Show student details
    def show_details(self):
        print("\nStudent Details")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    # Find student using roll number
    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll_number == roll:
                return student
        return None

    # Add new student
    @classmethod
    def add_student(cls):
        name = input("Enter student name: ")
        roll = int(input("Enter roll number: "))
        marks = int(input("Enter student marks: "))
        student = cls(name, roll, marks)
        cls.all_students.append(student)

        print(f"\nStudent '{name}' added successfully!")

    # Update student marks
    @classmethod
    def update_student_marks(cls):
        roll = int(input("Enter student roll number to update marks: "))
        student = cls.find_student_by_roll(roll)
        if student:
            new_marks = int(input("Enter new marks: "))
            student.update_marks(new_marks)
            print(f"\nMarks updated successfully for Roll Number {roll}!")
        else:
            print("Student not found.")

    # Show all students
    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("\nNo students found.")
            return
        print("\n========== All Students ==========")
        for student in cls.all_students:
            student.show_details()


# Menu function
def menu():
    while True:
        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show All Students")
        print("4. Exit")
        choice = input("Enter your option (1-4): ")
        if choice == "1":
            Student.add_student()
        elif choice == "2":
            Student.update_student_marks()
        elif choice == "3":
            Student.show_all_students()
        elif choice == "4":
            print("\nExiting Student Management System, Bye!!")
            break
        else:
            print("Invalid choice, please try again.")


# Start program
if __name__ == "__main__":
    menu()