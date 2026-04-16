import shlex
tasks = []
def filter_info(info):
    info
    if len(info) > 0:
        main_command = info[0]
        
        if main_command == "add":
            if len(info) < 2:
                 adding_info() 
            else:
                sub_info = info[1]
                adding_info(sub_info) #so it just like filters the first command
        elif main_command == "update":
            if len(info) < 3:
                update_fuc()
            else:
                task_id = info[1]
                new_text = info[2]
                update_fuc(task_id, new_text)
        elif main_command == "delete":
            if len(info) < 2:
                delete_fuc()
            else:
                sub_info = info[1]
                delete_fuc(sub_info)
        elif main_command == "mark-in-progress":
            print(f"adding task")# mark the task in progress
        elif main_command == "mark-done":
            print(f"adding task")#marks it done
        elif main_command == "list":
            listing_info() #list all the tasks
        else:
            print("unknow command! ")

def adding_info(follow_up=None):
    if follow_up == None:
      print("Enter task: to add")
    else:
        new_task = {
            "id": len(tasks) + 1,
            "description": follow_up,
            "status":"todo"
        }
        formating_data(new_task)
        tasks.append(new_task)
        print(f"Task added successfully: {new_task}")
 
def listing_info():
    if len(tasks) == 0 :
        print("No task yet")
    else:
        for task in tasks:
            print(formating_data(task))
run = True
def delete_fuc(index=None):
    if index is None:
        print("add the id:")
        return
    try:
        i = int(index) - 1
        deleted = tasks.pop(i)

        for position, task in enumerate(tasks, start=1):
            task["id"] = position

        print(f"Deleted task: {deleted}")
    except (TypeError, ValueError, IndexError):
        print("Please enter a valid task id")
        
def update_fuc(id=None, new_text=None):
    if id is None or new_text is None:
        print("Please provide task id and new description")
        return

    try:
        a = int(id)
    except (TypeError, ValueError):
        print("Please enter a valid task id")
        return

    for task in tasks:
        if task["id"] == a:
            task["description"] = new_text
            print(f"Task updated successfully: {task}")
            return

    print("Task not found")
        


def formating_data(info_filter):
    return f"ID: {info_filter['id']} | Description:{info_filter['description']} | Status: {info_filter['status']}"

print("========================================")
print("       🌍 Welcome to Tasknote CLI      ")
print("========================================")
print("\n Type /help to see available commands")
print("Type quit to exit")

def slicing_info(slicer):
     
    slicer = slicer.strip().lower()
    if slicer == "/help":
        commands = [
    'add "Buy groceries"',
    'update 1 "Buy groceries and cook dinner"',
    'delete 1',
    'mark-in-progress 1',
    'mark-done 1',
    'list',
    'list done',
    'list todo',
    'list in-progress'
]
        print("Available commands:")
        for command in commands:
            print(f"{command}")
    elif slicer == "quit":
        print("Quiting the program ....................")
        return False
    else:
        filtered = shlex.split(slicer)
        filter_info(filtered)
        return True
    
while True:
 task_info = input(">:")
 if run == True:
  run = slicing_info(task_info)
 else:
     break



