def task():
    tasks = [];
    print("=======================================");
    print("-- Welcome to the Task Managment App --");
    print("=======================================");
    
    total_task = int(input("Enter how many tasks you want to add  : "));
    
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ");
        tasks.append(task_name);

    
    while True:
        opertaion = int(input("Enter 1 to Add \nEnter 2 to Update \nEnter 3 to Delete \nEnter 4 to View \nEnter 5 to Exit/Stop : "));

        if(opertaion == 1):
           add =  input("Enter task you want to add : ");
           tasks.append(add);
           print(f"{add} task has been successfully Added");
        elif(opertaion == 2):
            update_val = input("Enter the task you want to update : ");
            if update_val in tasks:
                updated_task = input("Enter new task : ");
                ind = tasks.index(update_val);
                tasks[ind] = updated_task;
                print(f"Task Updated : {updated_task}");
            else:
                print("Please Enter a valid task");
                
        elif opertaion == 3:
            del_val = input("Which task you want to delete : ");
            if del_val in tasks:
                index = tasks.index(del_val);
                del tasks[index];
                print(f"Task {del_val} has been deleted successfully.")
            else:
                print("Please Enter a valid task");
        
        elif opertaion == 4:
            for task in tasks:
                print(task);
                
        elif opertaion == 5:
            print("closing the program.....")
            break;
        else:
            print("invalid operation");
task();