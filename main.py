from datetime import datetime

'''
Додаток, який буде зберігати нотатки

This is my note, that I am taking on my laptop
- Created on 17.10.2026 11:45

Зберігання даних у вигляді списку кортежів:
[("This is my note, that I am taking on my laptop", "17.10.2026 11:45")]
[("17.10.2026 11:45", "This is my note, that I am taking on my laptop")]

if note_data_one[1] > note_data_one[1]: - порівняння дат з різних кортежів
    ...

Зберігання даних у вигляді словника: (переваою словника є те, що можна не звертати увагу на порядок елементів)
{"text": "This is my note, that I am taking on my laptop", "creation_date": "17.10.2026 11:45"}
{"creation_date": "17.10.2026 11:45", "text": "This is my note, that I am taking on my laptop"}

if note_data_one["creation_date"] > note_data_one["creation_date"]: - порівняння дат з різних елементів словника
    ...

1) Створити словник нотаток та записати в нього інформацію
2) Написати функцію, яка буде виводити нотатку
3) Написати функцію, яка буде виводити всі нотатки
4) Написати цикл, який буде отримувати інформацію від користувача та реагувати на неї

'''

note_list = [] # [{"creation_date": "17.10.2026 11:45", "text": "This is my note, that I am taking on my laptop"}]
note_file = "notes.txt"

# Hello note;19.12


welcome_banner = r'''
  _    _      _                   ____        _   
 | |  | |    | |                 |  _ \      | |  
 | |__| | ___| |_ __   ___ _ __  | |_) | ___ | |_ 
 |  __  |/ _ \ | '_ \ / _ \ '__| |  _ < / _ \| __|
 | |  | |  __/ | |_) |  __/ |    | |_) | (_) | |_ 
 |_|  |_|\___|_| .__/ \___|_|    |____/ \___/ \__|
               | |                                
               |_|                                
'''

commands = '''
1) exit - to exit the application
2) add_note - to add a new note
3) print_note [i] - to print note number i
4) print_all - to print all notes
5) help - to print this menu
'''

def add_new_note(note_text) -> bool: 
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True

def print_note(index: int):
    note = note_list[index]
    # 17.10.2026 11:45 -> dd.mm.yyyy hh:mm
    formatted_creation_date = note['creation_date'].strftime("%d.%m.%Y %H:%M") # str f time -> string format time
    # str p time -> string parse time
    print(f"{note['text']}\n- Created on: {formatted_creation_date}\n")

def print_all_notes():
    for note_index in range(len(note_list)):
        print_note(note_index)


def save_notes():
    with open(note_file, 'w') as file:
        for note in note_list:
            file.write(f"{note["text"]};{note["creation_date"]}\n")

def read_notes() -> list[dict]:
    note_list = [] # оголошена в сердині функції і ніяк не пов'язана із зовнішньою змінною note_list
    with open(note_file) as file:
        for line in file:
            # Hello note;2026-10-17 19:01:31.921767
            text, date = line.strip().split(';')
            creation_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"text": text, "creation_date": creation_date})
    return note_list

def init():
    global note_list
    note_list = read_notes()

    print(welcome_banner)
    print("\nHello and welcome to our app!\n")
    print(commands)
    print()

def main():
    while True:
        command, *args = input("Please enter command (enter 'exit' to stop): ").strip().split(' ') # print_note 1
        if command == 'exit':
            print('Goodbye!')
            save_notes()
            break
        elif command == 'add_note':
            text = input("Please enter note text: ")
            if add_new_note(text):
                print("\nNote added successfully!\n")
            else:
                print("\nError while adding a note!\n")
        elif command == "help":
            print(commands)
        elif command == "print_note":
            index = int(args[0]) - 1
            if index < 0 or index >= len(note_list):
                print("Please enter a valid note number")
                continue 
            print_note(index)


# text = input("Please enter note text: ")
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)

# print_all_notes()

init()
main()


# "   add_note 1 ".strip()
# "add_note 1"split(" ")
# ["add_note", "1"]
# command, *args = ["add_note", "1"]
# command = "add_note"
# *args = "1"

# пояснення принципу роботи *args
# list = [1, 2, 3, 4, 5]

# first, *second = list

# print(first) # 1
# print(second) # [2, 3, 4, 5]