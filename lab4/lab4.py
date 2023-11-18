user_keys = ['Name', 'Surname', 'Age', 'Address', 'Username', 'Password']
users = []

def add_user():
    new_user = {}
    for key in user_keys:
        value = input(f"Введите {key}: ")
        if key == 'Age':
            while not value.isdigit():
                value = input("Введите возраст числом: ")
        new_user[key] = value
    while any(user.get('Username') == new_user['Username'] for user in users):
        print("Пользователь с такой почтой уже существует.")
        new_user['Username'] = input("Введите другую почту: ")
    while len(new_user['Password']) <= 8:
        print("Пароль должен содержать более 8 символов.")
        new_user['Password'] = input("Введите пароль: ")
    users.append(new_user)
    print("Пользователь успешно добавлен.")

def delete_user():
    username = input("Введите почту пользователя для удаления: ")
    for user in users:
        if user['Username'] == username:
            users.remove(user)
            print("Пользователь удален.")
            return
    print("Пользователь с такой почтой не найден.")

def view_users():
    if not users:
        print("Список пользователей пуст.")
    else:
        print("Список пользователей:")
        for user in users:
            print(user)

def login():
    username = input("Введите почту: ")
    password = input("Введите пароль: ")
    for user in users:
        if user['Username'] == username and user['Password'] == password:
            print("Вы успешно вошли в систему.")
            return
    print("Неправильная почта или пароль.")

while True:
    print("\nВыберите действие:")
    print("1. Добавить нового пользователя")
    print("2. Удалить пользователя")
    print("3. Посмотреть список пользователей")
    print("4. Войти в систему")
    print("5. Выйти из программы")

    choice = input("Введите номер действия: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        delete_user()
    elif choice == '3':
        view_users()
    elif choice == '4':
        login()
    elif choice == '5':
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите снова.")