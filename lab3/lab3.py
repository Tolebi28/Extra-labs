def get_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Вы ввели строку. Введите число, чтобы продолжить использование калькулятора.")

def main():
    while True:
        a = get_input('Insert a: ')
        b = get_input('Insert b: ')
        operation = input('Enter option (0 to exit): ')

        if operation == '0':
            break

        perform_operation(a, b, operation)

    print("Goodbye")

def perform_operation(a, b, operation):
    if operation == "1":
        Answer = a + b
        print(Answer)
    elif operation == "2":
        Answer = a - b
        print(Answer)
    elif operation == "3":
        Answer = a * b
        print(Answer)
    elif operation == "4":
        if b != 0:  # Check for division by zero
            Answer = a / b
            print(Answer)
        else:
            print("Cannot divide by zero.")
    elif operation == "5":
        for _ in range(a):
            print(a, end=' ')
            a, b = b, a + b
        print()
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
