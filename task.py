import shlex
import os
import json

tasks = []
FILE_NAME = "tasks.json"

def filter_info(info):
    """Routes the parsed user input to the correct function based on the command."""
    if len(info) > 0:
        main_command = info[0]
        
        if main_command == "add":
            if len(info) < 2:
                adding_info() 
            else:
                adding_info(info[1])

        elif main_command == "update":
            if len(info) < 3:
                update_fuc()
            else:
                update_fuc(info[1], info[2])

        elif main_command == "delete":
            if len(info) < 2:
                delete_fuc()
            else:
                delete_fuc(info[1])

        elif main_command == "mark-in-progress":
            if len(info) < 2:
                mark_in_progress()
            else:
                mark_in_progress(info[1], "in-progress")

        elif main_command == "mark-done":
            if len(info) < 2:
                mark_done()
            else:
                mark_done(info[1], "done")

        elif main_command == "list":
            if len(info) < 2:
                listing_info() 
            else:
                listing_info(info[1])
        else:
            print("Unknown command! Type /help for a list of commands.")

def adding_info(follow_up=None):
    """Creates a new task with a unique ID and saves it to the list."""
    if follow_up == None:
        print("Error: Please provide a task description.")
    else:
        new_task = {
            "id": len(tasks) + 1,
            "description": follow_up,
            "status": "todo"
        }
        tasks.append(new_task)
        save_tasks()
        print(f"Task added successfully: {new_task['description']}")

def listing_info(status=None):
    """Displays tasks, optionally filtered by their current status."""
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        found = False
        for task in tasks:
            if status is None or task["status"] == status:
                print(formating_data(task))
                found = True
        
        if not found:
            print(f"No tasks found with status: {status}")

def delete_fuc(index=None):
    """Removes a task by ID and re-indexes the remaining tasks to maintain order."""
    if index is None:
        print("Error: Please provide the task ID to delete.")
        return
    try:
        i = int(index) - 1
        deleted = tasks.pop(i)

        # Renumber IDs so they stay 1, 2, 3...
        for position, task in enumerate(tasks, start=1):
            task["id"] = position
        
        save_tasks()
        print(f"Deleted task: {deleted['description']}")
    except (TypeError, ValueError, IndexError):
        print("Error: Please enter a valid task ID.")

def update_fuc(id=None, new_text=None):
    """Updates the description of an existing task found by ID."""
    if id is None or new_text is None:
        print("Error: Provide both task ID and new description.")
        return

    try:
        target_id = int(id)
    except (TypeError, ValueError):
        print("Error: Invalid task ID.")
        return

    for task in tasks:
        if task["id"] == target_id:
            task["description"] = new_text
            save_tasks()
            print(f"Task {target_id} updated successfully.")
            return

    print("Task not found.")

def mark_in_progress(id=None, status=None):
    """Updates a task status to 'in-progress'."""
    if id is None or status is None:
        print("Error: Please provide a task ID.")
        return

    try:
        target_id = int(id)
    except (TypeError, ValueError):
        print("Error: Invalid task ID.")
        return

    for task in tasks:
        if task["id"] == target_id:
            task["status"] = status
            save_tasks()
            print(f"Task {target_id} is now in-progress.")
            return

    print(f"Error: Task {target_id} not found.")

def mark_done(id=None, status=None):
    """Updates a task status to 'done'."""
    if id is None or status is None:
        print("Error: Please provide a task ID.")
        return

    try:
        target_id = int(id)
    except (TypeError, ValueError):
        print("Error: Invalid task ID.")
        return

    for task in tasks:
        if task["id"] == target_id:
            task["status"] = status
            save_tasks()
            print(f"Task {target_id} marked as done.")
            return

    print(f"Error: Task {target_id} not found.")

def ensure_file():
    """Checks if the JSON database exists, creating it if necessary."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)

def save_tasks():
    """Writes the current task list to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    """Loads tasks from the JSON file into the program memory."""
    global tasks
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []

def formating_data(task):
    """Returns a string formatted for display in the terminal."""
    return f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}"

def slicing_info(user_input):
    """Parses input string and handles system commands like help and quit."""
    clean_input = user_input.strip().lower()
    
    if clean_input == "/help":
        commands = [
            'add "Task description"',
            'update 1 "New description"',
            'delete 1',
            'mark-in-progress 1',
            'mark-done 1',
            'list',
            'list done',
            'list todo',
            'list in-progress'
        ]
        print("\nAvailable commands:")
        for cmd in commands:
            print(f" - {cmd}")
        return True
    
    elif clean_input == "quit":
        print("Exiting Tasknote... Goodbye!")
        return False
    
    else:
        # Uses shlex to handle quoted descriptions correctly
        filtered = shlex.split(clean_input)
        filter_info(filtered)
        return True

# Initialize program
ensure_file()
load_tasks()

print("========================================")
print("      🌍 Welcome to Tasknote CLI      ")
print("========================================")
print("\nType /help to see commands or 'quit' to exit")

run = True
while run:
    task_info = input(">: ")
    run = slicing_info(task_info)