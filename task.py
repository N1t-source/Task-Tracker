def filter_info(info):
    if info == "add":
        print(f"adding task") #so it just like filters the first command
    elif info == "update":
       print(f"adding task")#so it updates the info or modify it with a new info
    elif info == "delete":
        print(f"adding task") #deletes the info
    elif info == "mark-in-progress":
        print(f"adding task")# mark the task in progress
    elif info == "mark-done":
        print(f"adding task")#marks it done
    elif info == "list":
        print(f"adding task") #list all the tasks
    else:
        print("unknow command! ")


def slicing_info(slicer):
    



task_info = input("Enter your task:")
filter_info(task_info)
