from colorama import init, Fore, Back, Style
from crud import add_task, view_task, delete_task, mark_task_complete
import random, time

def main():
    file_path = 'todolist.json'
    loop = True
    
    while loop :   
        simbol = random.choice([f"✣{Fore.LIGHTYELLOW_EX}",f"✣{Fore.LIGHTGREEN_EX}",f"✣{Fore.LIGHTCYAN_EX}",f"✣{Fore.LIGHTBLACK_EX}",f"✣{Fore.LIGHTMAGENTA_EX}",f"✣{Fore.LIGHTBLUE_EX}",f"✣{Fore.LIGHTRED_EX}"])
        print("\n"+ f"{simbol*30}{Style.RESET_ALL}✣{Fore.WHITE}")
        print(f"{"  "*6} Menu{Fore.MAGENTA}\n")
        print(f"{"  "*1} {Fore.YELLOW}1.{Style.RESET_ALL} View Tasks")
        print(f"{"  "*1} {Fore.YELLOW}2.{Style.RESET_ALL} Add Task")
        print(f"{"  "*1} {Fore.YELLOW}3.{Style.RESET_ALL} View Delete Task")
        print(f"{"  "*1} {Fore.YELLOW}4.{Style.RESET_ALL} Mark Task as Complete")
        print(f"{"  "*1} {Fore.YELLOW}5.{Style.RESET_ALL} Exit")
        print(f"{simbol*30}{Style.RESET_ALL}✣{Fore.WHITE}")
        time.sleep(1)
        chouce = input("\n  Please select : ")
        if chouce == "1":
            status = True
            while status:
                view_task(file_path)
                time.sleep(1)
                status = input(f"\n\n{"  "*1}{Style.RESET_ALL} Exit [y/n] :")
                if(status == "y"):
                    status = False
                else:
                    status = True
        elif chouce == "2":
            status = True
            while status:
                print(f"\n\n{"  "*5} Create Task")
                task = input(f"{Fore.YELLOW}#Note{Style.RESET_ALL} :")
                add_task(file_path, task)
                time.sleep(1)
                status = input(f"\n\n{"  "*1}{Style.RESET_ALL} Exit [y/n] :")
                if(status == "y"):
                    status = False
                else:
                    status = True
        elif chouce == "3":
            status = True
            while status:
                view_task(file_path)
                time.sleep(1)
                task_number = input("\n What number do you want to delete? ")
                delete_task(file_path,int(task_number))
                status = input(f"\n\n{"  "*1}{Style.RESET_ALL} Exit [y/n] :")
                if(status == "y"):
                    status = False
                else:
                    status = True
        elif chouce == "4":
            status = True
            while status :
                view_task(file_path)
                time.sleep(1)
                task_number = input("\n what number is finished :")
                mark_task_complete(file_path, int(task_number))
                status = input(f"\n\n{"  "*1}{Style.RESET_ALL} Exit [y/n] :")
                if(status == "y"):
                    status = False
                else:
                    status = True
        elif chouce == "5":
            exit()
            loop = False
        else :
            print(f"{Fore.YELLOW}You can only select the above options!{Style.RESET_ALL}")
        
if __name__ == "__main__":
    main()