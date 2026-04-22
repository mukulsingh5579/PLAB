#To-Do List (File Handling + Persistent Storage)
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No tasks found.")

while True:
    choice = input("1.Add 2.View 3.Exit: ")
    
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break