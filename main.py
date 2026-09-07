collections = ['task1','task2'] #list
is_start = True #flag
while is_start:
    print("1 - показать задачи| 2 - добавить заметку")
    choice_user = input("введите ваш выбор")
    match choice_user:
        case 1:
            print(collections)
        case 2:
            collections.append('task3')
            print(collections)
            case _:
            print('Такого пункта нет!')
