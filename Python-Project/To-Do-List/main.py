tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        index = int(input("Enter task index to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
