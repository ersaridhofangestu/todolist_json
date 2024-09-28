from script import load_data, save_data
from colorama import init, Fore, Back, Style
import time

def add_task(file_path, task):
    data = load_data(file_path)
    print(len(task))
    if  len(task) >= 3 :
        data.append({"task": task,"completed": False})
        save_data(file_path, data)
        time.sleep(1)
        print(f"({Fore.GREEN}success{Style.RESET_ALL}) - task additional.")
    else :
        print(f"({Fore.RED}invalid{Style.RESET_ALL}) - value must be greater than or equal to three")
    
def view_task(file_path):
    data = load_data(file_path)
    if data :
        print(f"\n\n{"  "*4} List Taks")
        for idx, task in enumerate(data, start=1):
            status = f"{Fore.GREEN}✔ Done{Style.RESET_ALL}" if task["completed"] else f"{Fore.RED}🗙 Not Done{Style.RESET_ALL}"
            print(f"{Fore.YELLOW}{idx}{Style.RESET_ALL}. {task["task"]} - {status}")
    else :
        time.sleep(1)
        print(f"({Fore.RED}invalid{Style.RESET_ALL}) - No tasks found.")
            
def delete_task(file_path, task_number):
    data = load_data(file_path)
    if 0 < task_number <= len(data):
        remove_task = data.pop(task_number - 1)
        save_data(file_path, data)
        time.sleep(1)
        print(f"({Fore.GREEN}success{Style.RESET_ALL}) - task '{remove_task['task']}' deleted.")
    else:
        time.sleep(1)
        print(f"({Fore.RED}invalid{Style.RESET_ALL}) - taks number found.")

def mark_task_complete(file_path,  task_number):
    data = load_data(file_path)
    if 0 < task_number <= len(data):
        data[task_number - 1]["completed"] = True
        save_data(file_path, data)
        time.sleep(1)
        print(f"({Fore.GREEN}success{Style.RESET_ALL}) - '{data[task_number - 1]['task']}' marked as compete.")
    else:
        time.sleep(1)
        print(f"({Fore.RED}invalid{Style.RESET_ALL}) - taks number found.")
        
    