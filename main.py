class Book:
    count = 0

    def __init__(self,
                 name: str,
                 author: str,
                 date_of_pub: str,
                 status='Доступна'):
        self.name = name
        self.author = author
        self.date_of_pub = date_of_pub
        self.status = status
        books.append(self)
        Book.count += 1
    
    # Получение информации о книгах
    def get_info_books(self):
        for index, book in enumerate(books):
            print(f'{index + 1}. {book.name}')
        return

    # Информация о книге
    def get_info_book(self):
        return f'Название книги: {self.name}\n'\
                f'Автор: {self.author}\n'\
                f'Дата публикации: {self.date_of_pub}\n'\
                f'Статус: {self.status}\n'

    # Бронирование книги
    def book_booking(self, choice_action_book):
        global reserved_book
        global books
        ordinal_number: int = 0
        if books[choice_action_book - 1].status != 'Забронирована':
            # Добавления забронированной книги в словарь с порядковыми номерами
            reserved_book[ordinal_number] = books[choice_action_book - 1]
            books[choice_action_book - 1].status = 'Забронирована'
            print('Книга забронирована\n')
            return True
        elif books[choice_action_book - 1].status == 'Забронирована':
            print('Книга уже забронирована!\n')
            return False

    # Показ забронированных книг
    def view_booking_book(self):
        # Переменная для отслеживания факта наличия забронированных книг
        global has_reserved_books
        has_reserved_books = False
        for index, book in enumerate(books):
            # Вывод всех забронированных книг
            if book.status == 'Забронирована':
                print(f'{index + 1}. {book.get_info_book()}')
                has_reserved_books = True
                print('\n0. Назад')
                print('-'*30)
        if not has_reserved_books:
            print('Забронированных книг нет!\n')

    # Пользователь возвращает книгу в библиотеку
    def return_book(self):
        global obj_book
        global reserved_book
        global books
        global choice_book
        global has_reserved_books
        # Вывод на экран забронированных книг
        obj_book.view_booking_book()
        # Проверка на присутствие забронированных книг
        if reserved_book:
            try:
                while True:
                    print('Выберите книгу, которую хотите вернуть: ')
                    choice_book_to_return = int(input('\n> '))
                    print('-'*30)
                    if choice_book_to_return - 1 in reserved_book:
                        reserved_book[choice_book_to_return - 1].status = 'Доступна'
                        print('Книга возвращена!')
                        print('-'*30)
                        break
                    elif not choice_book_to_return:
                        break
                    else:
                        print('Такого номера нет!')
            except ValueError:
                print('Введите число!')
        else:
            print('-'*30)


class UserManager:
    global password

    # Пользователь выбирает свою роль
    def select_role(self):
        global rule
        global menu
        while True:
            try:
                print('1.Пользователь\n'
                      '2.Администратор')
                print('-'*30)
                print('Выберете свою роль:')
                choice = int(input('\n> '))
                print('-'*30)
            except ValueError:
                print('Введите число!')
            if choice == 1:
                rule = 'user'
                break
            elif choice == 2:
                write_password = input('Введите пароль администратора'
                                       '(Пароль: 123): \n> ')
                print('-'*30)
                # Проверка пароля
                if user_manager.correct_password(password, write_password):
                    rule = 'admin'
                    break
                else:
                    print('Пароль неверный')
            else:
                print('Такого числа нет!')
                print('-'*30)
        menu.view_menu()
        menu.choice_menu()

    # Проверка пароля
    def correct_password(self, write_pass, correct_pass):
        if write_pass == correct_pass:
            return True
        else:
            return False


class User:

    # Пользователь получает книгу
    def get_book(self):
        pass


class Administrator(User):

    # Администратор добавляет книгу
    def add_book(self):
        print('Введите название книги: ')
        name = input('> ')
        print('-'*30)
        print('Введите автора: ')
        author = input('> ')
        print('-'*30)
        print('Введите год публикации: ')
        date_of_pub = input('> ')
        print('-'*30)
        add_book = Book(name, author, date_of_pub)
        return 'Книга успешно добавлена!'

    # Администратор удаляет книгу
    def delete_book(self):
        global books
        obj_book.get_info_books()
        print('-'*30)
        print('Выберите книгу которую хотите удалить: ')
        while True:
            try:
                number = int(input('\n> '))
                if number - 1 in range(len(books)):
                    del books[number - 1]
                    print('Книга удалена!')
                    print('-'*30)
                    break
                else:
                    print('Такого числа нет!')
                    print('-'*30)
            except ValueError:
                print('Введите число!')
                print('-'*30)
        return

class MainMenu:
    # Отображение меню
    def view_menu(self):
        print(
            '1. Просмотреть книги',
            '2. Вернуть книгу',
            sep="\n"
            )
        if rule == 'admin':
            print(
                '3. Добавить книгу',
                '4. Удалить книгу',
                sep="\n"
            )
        print('\n0. Назад')
        print('-'*30)

    # Пользователь выбирает пункт меню
    def choice_menu(self):
        global obj_book
        try:
            print('Выберите действие: ')
            choice_menu = int(input('\n> '))
            print('-'*30)
            if choice_menu == 1:
                if books:
                    # Пользователь выбирает книгу и действие над ней
                    while True:
                        obj_book.get_info_books()
                        print('\n0. Назад')
                        print('-'*30)
                        if menu.choice_book():
                            break
                    print('-'*30)
                    # Вывод информации о книге
                    print(books[choice_book - 1].get_info_book())
                    print('-'*30)
                    menu.book_menu()
                else:
                    print('Библиотека пуста!')
                    print('-'*30)
            elif choice_menu == 2:
                obj_book.return_book()
                # Пользователь выбирает какую книгу он хочет вернуть
            elif choice_menu == 3:
                if rule == 'admin':
                    print(administrator.add_book())
                    print('-'*30)
                else:
                    print('Такого пункта в меню нет!')
                    print('-'*30)
            elif choice_menu == 4:
                if rule == 'admin':
                    print(administrator.delete_book())
                    print('-'*30)
                else:
                    print('Такого пункта в меню нет!')
                    print('-'*30)
            elif choice_menu == 0:
                user_manager.select_role()
            else:
                print('Такого пункта в меню нет!')
        except ValueError:
            print('Введите число')

    # Пользователь выбирает книгу и действие над ней
    def choice_book(self):
        global choice_book
        correct_book_number = False
        try:
            print('Выберите книгу:')
            choice_book = int(input('\n> '))
        except ValueError:
            print('Введите число!')
        if choice_book >= 1 and choice_book <= len(books):
            correct_book_number = True
            return correct_book_number
        elif choice_book == 0:
            menu.view_menu()
            menu.choice_menu()
        else:
            print('Такого номера нет!')
            print('-'*30)

    # Действие над книгой
    def book_menu(self):
        while True:
            try:
                print('1. Забронировать книгу')
                print('\n0. Назад')
                print('-'*30)
                print('Выберите действие: ')
                choice_action_book = int(input('\n> '))
                print('-'*30)
                # Пользователь бронирует книгу
                if choice_action_book == 1:
                    obj_book.book_booking(choice_book)
                    break
                elif choice_action_book == 0:
                    break
                else:
                    print('Такого пункта меню нет!')
            except ValueError:
                print('Введите число!')


if __name__ == '__main__':
    books = []
    reserved_book = {}
    obj_book = Book(name='Война и мир',
                    author='Лев Толстой',
                    date_of_pub='1869')
    obj_book = Book(name='Атлант расправил плечи',
                    author='Айн Рэнд',
                    date_of_pub='1957')
    obj_book = Book(name='11/22/63',
                    author='Стивен Кинг',
                    date_of_pub='2011')
    # Добавление новой книги от администратора
    administrator = Administrator()
    # Пароль для входа администратора
    password: str = '123'
    menu = MainMenu()
    user_manager = UserManager()
    while True:
        user_manager.select_role()
        menu.view_menu()
        menu.choice_menu()
