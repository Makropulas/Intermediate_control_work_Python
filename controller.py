import model
import view


def action():
    return input('Введите номер действия: ')


def menu():
    model.clear_console()
    view.print_menu()
    act = action()
    if act == '1':
        model.clear_console()
        model.add_note()
        waiting_for_input()
    elif act == '2':
        submenu()
    elif act == '3':
        exit()
    else:
        model.clear_console()
        print('\nНеверная команда. Вы будете возвращены в главное меню')
        waiting_for_input()


def submenu():
    model.clear_console()
    model.show_all_notes()
    view.print_submenu()
    act = action()
    if act == '1':
        model.open_note()
        waiting_for_input()
        submenu()
    elif act == '2':
        model.edit_note()
        waiting_for_input()
        submenu()
    elif act == '3':
        model.delete_note()
        waiting_for_input()
        submenu()
    elif act == '4':
        model.sort_notes_by_date()
        waiting_for_input()
        submenu()
    elif act == '5':
        print()
    else:
        print('\nНеверная команда')
        waiting_for_input()
        submenu()


def waiting_for_input():
    print()
    view.pause()
