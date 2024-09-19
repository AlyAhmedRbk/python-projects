students = {}


def add_std(name, grade):
    students[name] = grade;
    print(f"Student {name} with {grade} added!");
    print(students);
    
def update_std():
    name = input("Enter student name to update data : ");
    
    if name in students:
        grade = input(f"Enter new grade for {name} : ");
        students[name] = grade;
        print(f"Student {name} grade Udated Successfully!");
    else:
        print(f"student {student} not found");

def delete_std():
    name = input("Enter student name to delete records : ");
    if name in students:
        del students[name];
        print(f"Student {name} deleted successfully");
    else: 
        print("Student Not Found!");

def view_all():
    print(students);

def main():
    while True:
        print("----------------------------------")
        print("---- Student Managment System ----")
        print("----------------------------------")
        print("1 - Add Student");
        print("2 - View All Students");
        print("3 - Delete Student");
        print("4 - Update Student");
        print("5 - Exit");
        
        choise = int(input("Please Select an Option : "));
        
        if choise == 1:
            name = input("Enter Student Name : ");
            grade = input("Enter Student Grade : ");
            add_std(name, grade);
        elif choise == 2:
            view_all();
        elif choise == 3:
            delete_std();
        elif choise == 4:
            update_std();
        elif choise == 5:
            print("Closing App!")
            break;
        else:
            print("Please enter a valid choise");

main();