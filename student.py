class Student:
    all_students=[]
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks

    def update_marks(self,new_marks):
        self.marks=new_marks

    @classmethod
    def find_student_by_roll(cls,roll):
        for Student in cls.all_students:
            if Student.roll_number==roll:
                return Student
            return None
        


    # @classmethod
    def add_student(cls):
        name=input("Enter student name: ")
        roll=eval(input("Enter roll number: "))
        marks=eval(input("Enter student marls: "))
        student=cls(name,roll,marks)
        cls.all_students.append(student)
        print(f"student {name} added successfully!! ")

    @classmethod
    def update_student_marks(cls):
        roll=int(input("Enter Student roll number to update marks: "))
        Student=cls.find_student_by_roll(roll)
        if Student:
            new_marks=int(input("Enter new marks: "))
            Student.update_marks(new_marks)
        else:
            print("Student not found.")




    

def menu():
        while True:
            print("\n==========Student Managenemnt system==========")
            print("1. Add student")
            print("2. Update Marks")
            print("3. Show all Student")
            print("4. Exit")

            choice=int(input("Enter your option(1-4): "))
            if choice=="1":
                Student.add_student()
            elif choice=="2":
                Student.update_student_marks()
            elif choice=="3":
                Student.show_all_students()
            elif choice=="4":
                print("Exiting Student Management system, Bye!!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__=="__main__":
    menu()

        