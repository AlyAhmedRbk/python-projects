contacts = {}

while(True):
    print("--------------------------------");
    print("---- Contact Book App Menu -----");
    print("--------------------------------");
    print("1. Create Contact");
    print("2. View Contact");
    print("3. Update Contact");
    print("4. Delete Contact");
    print("5. Search Contact");
    print("6. Count Contact");
    print("7. Exit");
    
    choice = int(input("Enter Your Choice = "));
    
    if(choice == 1):
        name = input("Enter new name : ");
        if name in contacts:
            print(f"Contact name {name} already exists");
        else:
            age = input("Enter Age : ");
            email = input("Enter Email : ");
            phone = input("Enter Phone : ");
            contacts[name] = {"age": int(age), "email":email, "phone" : phone};
    elif (choice == 2):
        name = input("Enter the name to view contact : ");
        if name in contacts:
            print(f"{name} found");
            contact = contacts[name];
            print(f"Name : {name}, Age : {age}, Email : {email}, Phone : {phone}");
        else:
            print("Contact Not Found!");
    
    elif (choice == 3):
        name = input("Enter name to update data : ");   
        if (name in contacts):
            name = input("Enter new name : ");
            age = input("Enter new Age : ");
            email = input("Enter new Email : ");
            phone = input("Enter new Phone : ");     
            contacts[name] =  {"age": int(age), "email":email, "phone" : phone};
            print("Data Updated Successfully!")
        else:
            print("Contact Not Found!");    
    
    elif (choice == 4):
        name = input("Enter name to delete contact : ");
        
        if name in contacts:
            del contacts[name];
            print(f"Contact {name} deleted successfully!");
        else:
            print("Contact Not Found!");
    
    elif (choice == 5):
        search_name = input("Enter name to delete contact : ");
        found = False;
        
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print("Contact Found!");
                print(f"Name : {name}, Age : {age}, Email : {email}, Phone : {phone}");
                found = True;
        if not found:
            print("Contact Not Found!");
    
    elif (choice == 6):
        print(f"Total contacts in your book is : {len(contacts)}");
        
    elif (choice == 7):
        print("Thanks for using our app");
        break;
    else:
        print("Please Enter a valid Option");