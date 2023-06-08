import csv
import os
from datetime import datetime as dt

notes = 'Notes.csv'

def save_data_to_file(file_name, header, body):
    uid = generate_id()
    with open(file_name, 'a', newline='', encoding='UTF8') as file:
        now = dt.now()
        note = [uid, header, body, now.strftime('%d.%m.%y'), now.strftime('%X')]
        writer = csv.writer(file, delimiter=';')
        writer.writerow(note)


def add_note():
    save_data_to_file(notes, input("Введите заголовок заметки: "), input("Введите тело заметки: "))


def show_all_notes():
    if os.path.isfile(notes) and os.stat(notes).st_size==0:
        with open(notes, "r", newline="", encoding='UTF8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                print(f'Id: {row[0]}, Заголовок: {row[1]}\nЗаметка: {row[2]}\nПоследнее изменение: {row[3]} {row[4]}\n\n')
    else:
        print("Нет заметок")

def generate_id():
    max = 1
    if os.path.isfile(notes):
        with open(notes, "r", newline="", encoding='UTF8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if int(row[0]) >= max:
                        max = int(row[0]) + 1
        return max
    else:
        return max