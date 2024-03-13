tasks = []


def add_task(task):
  tasks.append(task)

def remove_task(task):
  tasks.remove(task)

def view_tasks():
  print(tasks)

def task_manager():
    while True:
        action = input("What do you want to do (add, remove, view, exit)?: ")
        if action == 'exit':
            break
        if action != 'view' : task_name = input("Task name please?: ")
        if action == 'add':
            add_task(task_name)
        elif action == 'remove':
            remove_task(task_name)
        elif action == 'view':
            view_tasks()
        else:
            print('Invalid action')


task_manager()