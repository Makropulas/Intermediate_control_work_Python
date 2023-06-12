import csv
import os
from datetime import datetime as dt

notes = 'Notes.csv'
now = dt.now()

def save_data_to_file(file_name, header, body):
    uid = generate_id()
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        note = [uid, header, body, now.strftime('%d.%m.%Y'), now.strftime('%X')]
        writer = csv.writer(file, delimiter=';')
        writer.writerow(note)


def add_note():
    save_data_to_file(notes, input("\nВведите заголовок заметки: "), input("Введите тело заметки: "))


def show_all_notes():
    if os.path.isfile(notes) and os.stat(notes).st_size!=0:
        print("Заметки\n")
        with open(notes, "r", newline="", encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                print_noteslist(row)
    else:
        print("Нет заметок")


def open_note():
    searched_id = enter_id()
    count = 0
    with open(notes, "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] == searched_id:
                clear_console()
                print(f"Заметка {row[0]}\n")
                print_note(row)
                count += 1
    if count == 0:
        id_not_found()


def edit_note():
    searched_id = enter_id()
    count = 0
    with open(notes, "r", newline="", encoding='utf-8') as file:
        reader = list(csv.reader(file, delimiter=';'))
        for row in reader:
            if row[0] == searched_id:
                clear_console()
                print(f"Заметка {row[0]}\n")
                print_note(row)
                row[2] = input("Введите новое тело заметки: ")
                row[3] = now.strftime('%d.%m.%Y')
                row[4] = now.strftime('%X')
                confirm = input('Сохранить изменения? Если да, введите "Y": ')
                count += 1
    if count == 0:
        id_not_found()
        return
    if confirm.upper() == 'Y':
        with open(notes, "w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(reader)


def delete_note():
    searched_id = enter_id()
    count = 0
    with open(notes, "r", newline="", encoding='utf-8') as file:
        reader = list(csv.reader(file, delimiter=';'))
        for row in reader:
            if row[0] == searched_id:
                clear_console()
                print("\nВы точно хотите удалить эту заметку?\n")
                print_note(row)
                confirm = input('Если да, введите "Y": ')
                if confirm.upper() == 'Y':
                    reader.remove(row)
                    print("\nЗаметка успешно удалена\n")
                count += 1
    if count != 0:
        with open(notes, "w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(reader)
    else:
        id_not_found()


def sort_notes_by_date():
    searched_date = input("\nВведите дату в формате ДД.ММ.ГГГГ: ")
    print()
    count = 0
    with open(notes, "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[3] == searched_date:
                print_noteslist(row)
                count += 1
    if count == 0:
        print("Заметки с такой датой не найдены")


def enter_id():
    return input("\nВведите идентификатор заметки: ")


def id_not_found():
    print()
    print("Нет такого ID")


def print_note(row):
    print(f'Заголовок: {row[1]}\nЗаметка: {row[2]}\nПоследнее изменение: {row[3]} {row[4]}\n\n')


def print_noteslist(row):
    print(f'ID: {row[0]} | {row[1]} | {row[3]}')


def generate_id():
    max = 1
    if os.path.isfile(notes):
        with open(notes, "r", newline="", encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if int(row[0]) >= max:
                        max = int(row[0]) + 1
        return max
    else:
        return max


def clear_console():
    os.system('cls||clear')
