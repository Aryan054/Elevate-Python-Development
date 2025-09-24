# todo.py - Console-based To-Do List Application

import os

TODO_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file if it exists, otherwise return empty list"""
    tasks = []
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as file:
                tasks = [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    """Save tasks to file"""
    try:
        with open(TODO_FILE, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except Exception as e:
        print(f"Error saving tasks: {e}")

def display_tasks(tasks):
    """Display all tasks with numbering"""
    if not tasks:
        print("No tasks in your to-do list!")
        return
    
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("-----------------------")

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def remove_task(tasks):
    """Remove a task by its number"""
    display_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main function to run the to-do list application"""
    tasks = load_tasks()
    
    print("=== To-Do List Manager ===")
    print("Commands: view, add, remove, exit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == 'view':
            display_tasks(tasks)
        elif command == 'add':
            add_task(tasks)
        elif command == 'remove':
            remove_task(tasks)
        elif command == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid command! Use: view, add, remove, exit")

if __name__ == "__main__":
    main()