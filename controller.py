import model
import view


def waiting_for_input():
    print()
    view.pause()


while True:
    view.print_menu()
    action = int(input('Введите номер действия: '))
    print()

    match action:
        case 1:
            model.add_note()
            waiting_for_input()
        case 2:
            model.show_all_notes()
            waiting_for_input()
        case 3:
            open_note()
        case 4:
            delete_note()
        case 5:
            sort_to_date()
        case 6:
            break
        case None:
            print()
        case _:
            print('Неверная команда. Возврат в меню')
            print()
            view.pause()
