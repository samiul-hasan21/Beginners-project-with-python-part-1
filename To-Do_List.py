class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.\n")
            return

        print("Your Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")
        print()

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed!\n")
        else:
            print("Invalid task number. Please try again.\n")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!\n")
        else:
            print("Invalid task number. Please try again.\n")

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]
        print("All completed tasks cleared!\n")

def display_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Clear Completed Tasks")
    print("6. Exit")
    print()

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.\n")
            continue

        if choice == 1:
            task = input("Enter the task: ").strip()
            if task:
                todo_list.add_task(task)
            else:
                print("Task cannot be empty.\n")
        elif choice == 2:
            todo_list.view_tasks()
        elif choice == 3:
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                todo_list.mark_task_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.\n")
        elif choice == 4:
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.\n")
        elif choice == 5:
            todo_list.clear_completed_tasks()
        elif choice == 6:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
