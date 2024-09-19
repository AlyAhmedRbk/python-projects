import os;

def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"File name {filename} Created Successfully!");
    except FileExistsError:
        print(f"File name {filename} already Exisit");
    
    except Exception as e:
        print("An Error Occur While Creating File!")
    

def view_all_files():
    files = os.listdir();
    
    if not files:
        print("No File Found.");
    else:
        print("Files in directory");
        for file in files:
            print(file);

def delete_file(filename):
    try:
        os.remove(filename);
        print(f"{filname} is Deleted Successfully");
    except FileNotFoundError:
        print("File not Found");
    except Exception as e:
        print("An Error Occured");

def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read(); 
            print(f"Conntent Of '{filename}' :\n {content}");
    except FileNotFoundError:
        print(f"{filename} file not found!");
    except Exception as e:
        print("An Error Occured");
        
def edit_file(filename):
    try:
        with open(filename, "a") as f:
            content = input("Enter data to add : ");
            f.write(content + "\n");
            print(f"Content Added to {filename} successfully");
    except FileNotFoundError:
        print(f"{filename} file not found");
    except Exception as e:
        print("An Error Occured" , e);

def main():
    while True:
        print("---------------------------------");
        print("------  File Managment App ------");
        print("---------------------------------");
        print('1 - Create File');
        print('2 - View all File');
        print('3 - Delete File');
        print('4 - Read File');
        print('5 - Edit File');
        print("6 - Exit");
        
        choice = int(input("Please Enter your choice : "));
        
        if(choice == 1):
            filename = input("Enter the file name to create :  ");
            create_file(filename);
        elif (choice == 2):
            view_all_files();
        elif (choice == 3):
            filename = input("Enter the file name to delete : ");
            delete_file(filename)
        elif (choice == 4):
            filename = input("Enter the filename to read : ");
            read_file(filename);
        elif (choice == 5):
            filename = input("Enter the file name to edit : ");
            edit_file(filename);
        elif (choice == 6):
            print("Closing the app.");
            break;
        else:
            print("Please Select a valid number!");

if __name__ == "__main__":
    main();