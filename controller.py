import view


def start():
    user = view.identif_user()
    if user == 'учитель':
        act = view.action()
        if act == 1:
            subject = view.subject()
            path = str(subject) + '.txt'
            with open(path, 'r', encoding='utf-8') as file:
                list = file.readlines() #создаём список строк в файле (фамилии учеников)
                file.close()
                view.console(list) # выводим в консоль чтобы видеть какие ученики есть в базе
                student = view.last_name()
                grade = view.grade()
                with open(path, 'w', encoding='utf-8') as file:
                    for line in list:
                        if student in line:
                            line = line[:-1] + grade + ' ' + line[-1:] # ставим оценку к фамилии
                        file.writelines(line) # весь список с новой строкой перезаписываем в файл


        if act == 2:
            subject = view.subject()
            path = str(subject) + '.txt'
            with open(path, 'r', encoding='utf-8') as file:
                list = file.readlines()
                file.close()
                for line in list:
                    view.console(line) # построчно показывает оценки учеников по предмету
    

    else: 
        student = view.last_name()
        print(f'Дневник ученика: {student}')
        subjects = ['математика', 'история', 'литература', 'информатика']
        for subject in subjects:
            path = str(subject) + '.txt'
            view.console(subject)
            with open(path, 'r', encoding='utf-8') as file:
                list = file.readlines()
                file.close()
                for line in list:
                    if student in line:
                        print(line)
                        break


         

if __name__ == '__main__':
    start()

                



