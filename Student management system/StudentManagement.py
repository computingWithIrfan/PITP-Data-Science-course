import os

menu = {
    1 : "Add a Student.",
    2 : "View all student.",
    3 : "Search a student by name.",
    4 : "Update marks of a student.",
    5 : "Exit"
}
students = [
    {"name": "Alice", "age": 20, "marks": 88}
]

## Fucntion to update marks
def update_marks():
    print("*** Updating Marks ***")
    name = input("Enter the student name to update marks: ")
    matched = [st for st in students if st["name"].lower() == name.lower()]
    if not matched:
        print("⚠ No student found with that name.")
        return

    if len(matched) == 1:
        student = matched[0]
        print("Student found:")
        view_students([student])

        new_marks = int(input("Enter new marks: "))
        student["marks"] = new_marks
        print("✔ Marks updated successfully!")
        return
    
    print("Multiple students found with this name:")
    for i, st in enumerate(matched, start=1):
        print(f"{i}. {st['name']} | Age: {st['age']} | Marks: {st['marks']}")

    choice = int(input("Select the student number to update: "))
    if 1 <= choice <= len(matched):
        student = matched[choice - 1]
        new_marks = int(input("Enter new marks: "))
        student["marks"] = new_marks
        print("✔ Marks updated successfully!")
    else:
        print("❌ Invalid selection.")

## Function to search student
def search_student():
    print("*** Searched Students ***")
    name = input("Enter name to search : ")
    searched = []
    for st in students:
        if st['name'].lower() == name.lower():
            searched.append(st)
    view_students(searched)
        
## Function to display student on console
def view_students(std):
    print("*** Registered Students ***")
    print(f"{'Name':<10} | {'Age':<5} | {'Marks':<5}")
    print("-" * 28)

    for st in std:
        print(f"{st['name']:<10} | {st['age']:<5} | {st['marks']:<5}")

        
## Function to add student
def add_student():
    print("***ADD NEW STUDENT***")
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    marks = int(input("Enter marks : "))
    students.append({
        "name" : name,
        "age" : age,
        "marks" : marks
    })
    
## Function to display menu
def displayMenu(menu_bar):
    print("===================================")
    print("_____STUDENT MANAGEMENT SYSTEM_____")
    print("===================================")
    for i,m in menu_bar.items():
        print(i,m)
        

## For clearing screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

exit = True
while exit:
    clear_screen()
    displayMenu(menu)
    try:
        choice = int(input("Choose Option : "))
    except ValueError:
        print("❌ Please enter a valid number!")
        input("Press Enter to continue...")
        continue   
    
    match choice:
        case 1:
            add_student()
            input("Press Enter to continue...")
        case 2:
            view_students(students)
            input("Press Enter to continue...")
        case 3:
            search_student()
            input("Press Enter to continue...")
        case 4:
            update_marks()
            input("Press Enter to continue...")
        case 5:
            exit = False
            print("====> SYSTEM EXITED <====")
        case _:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")