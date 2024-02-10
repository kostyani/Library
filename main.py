class Book:

    def __init__(self, name, author, date_of_pub):
        self.name = name
        self.author = author
        self.date_of_pub = date_of_pub

# Получение информации о книгах
    def get_info(self):
        return f'Название книги: {self.name}\n'\
                f'Автор: {self.author}\n'\
                f'Дата публикации: {self.date_of_pub}'

class Administrator:
    # Администратор добавляет книгу
    def add_book(self, name, author, date_of_pub):
        obj_book = Book(name, author, date_of_pub)
        return obj_book
# Проверка пароля
def Correct_password(write_pass, correct_pass):
    if write_pass == correct_pass:
        return True
    else:
        return False

# Отображение меню
# У администраторов расширенное меню
def viev_menu():
    print(
        '1. Просмотреть книги'
        '2. Получить книгу'
        '3. Вернуть книгу'
        )
    if rule == 'admin':
        print(
            '4. Добавить книгу'
            '5. Удалить книгу'
        )
        
    


if __name__ == '__main__':
    # Создание объекта класса Book
    book1 = Book(name='Война и мир', author='Лев Толстой', date_of_pub='1869')
    # Пароль для входа администратора
    password = '123'
    # Пользователь выбирает свою роль
    while True:
        try:
            choice = int(input(
                                'Выберете свою роль:'
                                '\n1.Пользователь'
                                '\n2.Администратор'
                                '\n> ')
                                )
        except ValueError:
            print('Введите число!')
        if choice == 1:
            rule = 'user'
            break
        elif choice == 2:
            write_password = input('Введите пароль администратора: \n> ')
            # Проверка пароля
            if Correct_password(password, write_password):
                rule = 'admin'
                break
            else:
                print('Пароль неверный')
    try:
        viev_menu()
        choice_menu = int(input('Введит'))
    except ValueError:
        print('Введите число')
        
