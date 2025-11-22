from src.grade_manager import GradeManager
from src.utils import clear_screen, print_header
import time

def main():
    gm = GradeManager()
    
    while True:
        clear_screen()
        print_header()
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Add/Update Marks")
        print("4. View Topper")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            clear_screen()
            print_header()
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            if gm.add_student(roll, name, age, course):
                print("✅ Student added successfully!")
            else:
                print("❌ Roll No already exists!")
            time.sleep(2)

        elif choice == '2':
            clear_screen()
            print_header()
            print("\nAll Students:\n")
            gm.view_all()
            input("\nPress Enter to continue...")

        elif choice == '3':
            clear_screen()
            print_header()
            roll = input("Enter Roll No: ")
            subject = input("Enter Subject: ")
            marks = int(input("Enter Marks: "))
            if gm.update_marks(roll, subject, marks):
                print("✅ Marks updated!")
                gm.save_data()
            else:
                print("❌ Student not found or invalid marks!")
            time.sleep(2)

        elif choice == '4':
            clear_screen()
            print_header()
            topper = gm.get_topper()
            if topper:
                print("🏆 TOP PERFORMER 🏆")
                print(topper)
            else:
                print("No students yet!")
            input("\nPress Enter to continue...")

        elif choice == '5':
            roll = input("Enter Roll No to delete: ")
            if gm.delete_student(roll):
                print("✅ Student deleted!")
            else:
                print("❌ Student not found!")
            time.sleep(2)

        elif choice == '6':
            print("\nThank you for using the system!")
            print("Made by Rajat - VIT Bhopal ❤️")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()
```
