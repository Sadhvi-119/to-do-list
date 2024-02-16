# Simple To-Do List

def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Save and Quit")
    print("===========================")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\n===== To-Do List =====")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
        print("=======================")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def mark_completed(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            index = int(input("Enter the number of the task to mark as completed: ")) - 1
            if 0 <= index < len(todo_list):
                completed_task = todo_list.pop(index)
                print(f"Task '{completed_task}' marked as completed.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No tasks to mark as completed.")

def save_and_quit(todo_list, file_path):
    with open(file_path, 'w') as file:
        for task in todo_list:
            file.write(task + '\n')
    print("To-Do List saved. Goodbye!")

def main():
    file_path = "todo_list.txt"
    try:
        with open(file_path, 'r') as file:
            todo_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            save_and_quit(todo_list, file_path)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
