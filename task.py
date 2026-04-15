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
         print(f"adding task")#so it updates the info or modify it with a new info
        elif main_command == "delete":
            print(f"adding task") #deletes the info
        elif main_command == "mark-in-progress":
            print(f"adding task")# mark the task in progress
        elif main_command == "mark-done":
            print(f"adding task")#marks it done
        elif main_command == "list":
            print(f"adding task") #list all the tasks
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
        tasks.append(new_task)
        print(f"Task added successfully: {new_task}")
 
def listing_info():
    if len(tasks) == 0 or tasks == None:
        print("No task yet")
run = True


print("========================================")
print("       🌍 Welcome to Tasknote CLI      ")
print("========================================")
print("\n Type /help to see available commands")
print("Type quit to exit")

def slicing_info(slicer):
     
    slicer = task_info.strip().lower()
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
    
while run:
 task_info = input(">:")
 run = slicing_info(task_info)



