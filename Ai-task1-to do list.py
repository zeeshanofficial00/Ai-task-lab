
todo_list = []
def show_tasks():
    if not todo_list:
        print("\n✅ No tasks yet. Add some!")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
def add_task():
    task = input("\n✍️ Enter a new task: ")
    todo_list.append(task)
    print("✅ Task added successfully!")
def remove_task():
    show_tasks()
    try:
        task_no = int(input("\n❌ Enter task number to remove: "))
        removed = todo_list.pop(task_no - 1)
        print(f"🗑️ '{removed}' removed successfully!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number!")
def update_task():
    show_tasks()
    try:
        task_no = int(input("\n📝 Enter task number to update: "))
        new_task = input("🔁 Enter new task: ")
        todo_list[task_no - 1] = new_task
        print("✅ Task updated successfully!")
    except (ValueError, IndexError):
        print("⚠️ Invalid input!")
while True:
    print("\n========= TO-DO LIST MENU =========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("👉 Enter your choice (1-5): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("👋 Exiting... Have a productive day!")
        break
    else:
        print("⚠️ Invalid choice! Try again.")
