"""1.
collection = [] #list
is_start = True #flag

while (is_start):
    print("1 - показать заметки | 2 - добавить заметку")
    choice_user = input('Введите ваш выбор (1 или 2)')
    match int(choice_user):
        case 1:
            print(collection)
        case 2:
            collection.append('task')
            print(collection)
        case _:
            print('Такого пункта нет!')

2.
import os
import sys
import platform
import datetime

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
os_processor = platform.processor()
os_machine = platform.machine()
os_python_version = platform.python_version()
os_android = platform.android_ver()

now = datetime.datetime.now()
sys_in = sys.path
sys_platform = sys.platform
sys_version = sys.version

print(f"{os_name} \n" 
      f"{os_version} \n" 
      f"{os_arch} \n" 
      f"{now.year} \n" 
      f"{now.month} \n" 
      f"{now.day} \n" 
      f"{now.hour} \n"
      f"{now.minute} \n"
      f"{now.second} \n"
      f"{now.microsecond} \n" 
      f"{os_processor} \n" 
      f"{os_machine} \n" 
      f"{os_python_version} \n" 
      f"{os_android} \n")

Код выводит данные компьютера, такие как его имя, версия оп, время и т.д."""
import os
import processes

is_running = True
collection = [ ] # list

def show_collection(task_collection):
    print("=" * 30)
    for i, j in enumerate(task_collection):
        print(i + 1, j)
    print("=" * 30)

def show_menu():
    print("1 - посмотреть задачи \n"
          "2 - добавить задачу \n"
          "3 - редактировать задачу \n"
          "4 - удалить задачу \n"
          "0 - выход")

def show_message():
    input("Нажмите 'ENTER' для продолжения")

def check_confitm(select_task, task_list):
    if select_task.isdigit():
        if (int(select_task) > 0 and int(select_task) <= len(task_list)):
            return True
        else:
            print(f"Задачи с номером {select_task} нет в списке!")
            return False
    else:
        print(f"ведите именно номер задачи!")
        return False

def delete_tasks(task_collection):
    delete_task = input("Введите номер задачи для удаления: ")
    if check_confitm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача с номером {delete_task} успешно удалена!")

def edit_task(task_collection):
    select_task = input("Введите номер задачи: ")
    if check_confitm(select_task, task_collection):
        edit_name = input("Введите имя задачи")
        task_collection[int(select_task) - 1] = edit_name
        print(f"Задача с номером {edit_name} успешно изменена!")

def add_tasks(task_collection):
    add_task = input("Введите имя задачи для добавления: ")
    if add_task.startswith(' '):
        if len(add_task) < 2:
            print("Название не может быть пустым!")
        else:
            task_collection.append(f"Задача {len(task_collection) + 1}")
    else:
        task_collection.append(add_task)
        print(f"Задача '{add_task}' успешно добавлена!")

def main():
    global is_running
    while is_running:
        show_menu()
        choice_user = input("Введите свой выбор: ")
        task_collection = []

        name_file = 'saves.txt'
        file = open(name_file, 'r', encoding='utf-8')
        for line in file:
            task_collection.append(line.strip(' '))
            print(line)

        match str(choice_user):
            case '1':
                show_collection(task_collection)
                show_message()
                # print (f"TM PID {os.getpid()}")
                # print (f"TM PID {os.getppid()}")
                # processes.main()

            case '2':
                add_tasks(task_collection)
                name_file = 'saves.txt'
                file = open(name_file, 'w', encoding='utf-8')
                for task in task_collection:
                    file.write(f"{task}\n")

            case '3':
                show_collection(task_collection)
                edit_task(task_collection)

            case '4':
                show_collection(task_collection)
                delete_tasks(task_collection)

            case '0':
                is_running = False
                print("Выход")

            case _:
                print("Такого пункта нет!")

if __name__ == "__main__":
    main()
