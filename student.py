class Student:
    all_students=[]
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks

    # @classmethod
    # def add_student(cls):


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

        