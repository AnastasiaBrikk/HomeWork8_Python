def identif_user():
    user = input('Введите статус пользователя(ученик или учитель): ')
    return user.lower()

def action():
    act = int(input('Чтобы поставить оценку введите 1, чтобы посмотреть оценки ученика введите 2: '))
    return act

def subject():
    subject = str(input('Выберите предмет: '))
    return subject.lower()

def last_name():
    last_name = str(input('Введите фамилию ученика: '))
    return last_name

def grade():
    grade = input('Введите оценку от 1 до 5: ')
    return grade

def console(data):
    print(*data)

        

if __name__ == "__main__":
    print(identif_user())
    print(subject())


