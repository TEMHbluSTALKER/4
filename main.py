import re
import random
import time
#Функции
###################################################
def TaskSelection():
    print("Выберите номер задачи:\n"
          "1 - Угадайте число.\n"
          "2 - Повторяющиеся элементы в списке.\n"
          "3 - Выходные дни недели.\n"
          "4 - Студенты.")
    number = input()
    match number:
        case "1":
            GuessTheNumber()
        case "2":
            DuplicateElements()
        case "3":
            DaysOff()
        case "4":
            Students()
        case _:
            print("Введен неправильный номер.")
            TaskSelection()

###################################################
def GuessTheNumber():
    ListOfNumbers = list()
    for i in range(5):
        ListOfNumbers.append(random.randint(0, 9))
    while 1 == 1:
        try:
            Number = int(input('Введите целое число (от 0 до 9): '))
        except ValueError:
            print('Введено не число!')
        else:
            if ListOfNumbers.count(Number) == 0:
                print('Нет такого числа!')
            else:
                print('Поздравляю, Вы угадали число!')
            print('Сгенерированы числа: ', *ListOfNumbers)
            break
###################################################

def DuplicateElements():
    N = 10
    ListOfNumbers = list()
    for i in range(N):
        ListOfNumbers.append(random.randint(0, 9))
    print('Сгенерированы числа: ', *ListOfNumbers)
    DuplicateNumbers = []
    for i in range(N):
        Counter = 0
        for j in range(i, N):
            if ListOfNumbers[i] == ListOfNumbers[j]:
                Counter += 1
        if Counter > 1:
            DuplicateNumbers.append(ListOfNumbers[i])
    DuplicateNumbers = set(DuplicateNumbers)
    print('Повторяющиеся элементы:', *DuplicateNumbers)
###################################################

def DaysOff():
    while 1 == 1:
        try:
            Number = int(input('Введите количество выходных дней на неделе: '))
        except ValueError:
            print('Введено не число!')
        else:
            print('Введённое число: ', Number)
            break
    if Number >= 0 and Number <=7:
        Weekday = list()
        Weekend = list()
        Days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
        for i in range(7-Number):
            Weekday.append(Days[i])
        print('Ваши рабочие дни: ', *Weekday)
        for i in range(7-Number,7):
            Weekend.append(Days[i])
        print('Ваши выходные дни: ', *Weekend)
    else:
        print('В неделе не может быть', Number, 'выходных.')
###################################################

def Students():
    FirstGroup = ['Петров', 'Иванов', 'Сидоров', 'Ивушкин', 'Ижорский', 'Васин', 'Матросов', 'Федоров', 'Кущин', 'Фролов']
    SecondGroup = ['Кукушкин', 'Бочкарев', 'Усачев', 'Бунин', 'Толстой', 'Романов', 'Милиганов', 'Левин', 'Панов', 'Кучков']
    print('Студенты 1 группы:', *FirstGroup)
    print('Студенты 2 группы:', *SecondGroup)
    while 1 == 1:
        SelectedFrom1Group = list()
        for i in range(5):
            SelectedFrom1Group.append(random.randint(0, 9))
        SelectedFrom1Group = set(SelectedFrom1Group)
        if len(SelectedFrom1Group) == 5:
            break
    while 1 == 1:
        SelectedFrom2Group = list()
        for i in range(5):
            SelectedFrom2Group.append(random.randint(0, 9))
        SelectedFrom2Group = set(SelectedFrom2Group)
        if len(SelectedFrom2Group) == 5:
            break
    Team = list()
    for i in SelectedFrom1Group:
        Team.append(FirstGroup[i])
    for i in SelectedFrom2Group:
        Team.append(SecondGroup[i])
    tuple(Team)
    print('Студенты, выбранные из двух групп:', *Team)
    print('Количество студентов в команде (длина кортежа):', len(Team))
    print('Фамилии команды отсортированные по алфавиту:', sorted(Team))
    CounterIvanov = Team.count('Иванов')
    if CounterIvanov != 0:
        print('Студент Иванов входит в полученную команду.')
    else:
        print('Студент Иванов не входит в полученную команду.')
    print('Фамилия Иванов встречается:', CounterIvanov, 'раз.')
###################################################

#Основная программа
TaskSelection()
