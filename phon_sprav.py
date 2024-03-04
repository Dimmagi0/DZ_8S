
import time

def work_with_phonebook():
    choice = show_menu()
    phone_book = 'phonebook.txt'
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    while choice != 5:
        if choice == 1:      # 1. Отобразить весь справочник
            print_sprav(phone_book, fields)
        elif choice == 2:     # 2. Добавить абонента в справочник
            add_user(phone_book, fields)
        elif choice == 3:     # 3. Закончить работу
            break
        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Добавить абонента в справочник\n"
          "3. Закончить работу")
    choice = int(input('Введите номер действия: '))
    return choice


def print_sprav(filename, fields):          # 1. Отобразить весь справочник
    phone_book = read_txt(filename, fields)
    time.sleep(1)
    for i in phone_book:
        print(*i.values(), end='')


def add_user(filename, fields):           # 2. Добавить абонента в справочник
    record = {}
    contacts = []
    phone_book = read_txt(filename, fields)
    for i in fields:
        record[i] = input(f'{i}: ')
    phone_book.append(record)
    for i in phone_book:
        contacts.append(list(i.values()))
    writeToFile(filename, contacts)


def read_txt(filename, fields):

    with open(filename, 'r', encoding='utf-8') as phb:
        contacts = phb.readlines()
        phone_book = []

        for contact in contacts:
            record = dict(zip(fields, contact.split(', ')))
            phone_book.append(record)
    return phone_book


def writeToFile(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as phb:
        for contact in contacts:
            phb.write(', '.join(contact).strip() + '\n')


work_with_phonebook()