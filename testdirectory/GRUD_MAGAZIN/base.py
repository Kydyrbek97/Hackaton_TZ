from views import listing,retrieve,create_,update_,delete_

def base():
    print('Привет! Тебе доступны следующие функции:\n\tПолный список-1\n\tДетально-2\n\tСоздать-3\n\tОбновить-4\n\tУдалить-5')
    choice = input('Введите действия(1,2,3,4,5): ')

    if choice.strip() == '1':
        print(listing())
    elif choice.strip() == '2':
        print(retrieve())
    elif choice.strip() == '3':
        print(create_())
    elif choice.strip() == '4':
        print(update_())
    elif choice.strip() == '5':
        print(delete_())
    else:
        print('Неверный выбор!')
        
    answer = input('Хотите продолжить?(yes/no): ')
    if answer.lower().strip() == 'yes':
        base()
    else:
        print('Программа завершена!')
base()