def task():
    task =[]
    print ("-----welcome to the task manager-----")

    total_tasks = int(input("How many tasks do you want to add? "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter the name of task {i}: ")
        task.append(task_name)
    
    print("\nHere are your tasks:")

    while True:
        operation = input(f"Enter 1 to add a new tasks,\nEnter 2 to update your task,\nEnter 3 to remove a task,\nEnter 4 to view your task\n'Exit' to quit\n").lower()
        if operation == "1" :
            view = input ("Enter your new task\n")
            task.append(view)
            print(f"Task {view} added successfully!")
        
        elif operation == "2" :
            updated_value = input("Enter the task you want to update: ")
            if updated_value in task :
                new_value = input("Enter the new value for the task: ")
                ind = task.index(updated_value)
                task[ind] = new_value
                print(f"Task {updated_value} updated to {new_value} successfully!")

        elif operation == "3":
            remove = input("Enter the task you want to remove\n")
            if remove in task:
                task.remove(remove)
                print(f"Task {remove} removed successfully!")
            else:
                print(f"Task {remove} not found in the list.")
        
        elif operation == "4":
           print(f"Here are your current tasks:{task}")

        elif operation == "exit" :
            exit = input ("are you want to exit 'yes' or 'no'? ").lower()
            if exit() == "yes":
                print("Exiting the task manager. Goodbye!")
                break
        else:
            print("Invalid input. Please try again.")
        print("\nCurrent tasks:")

task()            