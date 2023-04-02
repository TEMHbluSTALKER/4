import re
import random
import time
#Функции
###################################################
def TaskSelection():
    print("Выберите номер задачи:\n"
          "1 - Угадайте число.\n"
          "2 - повторяющиеся элементы в списке.\n"
          "3 - Выходные дни недели.\n"
          "4 - Студенты.")
    number = input()
    match number:
        case "1":
            DivisionBy3()
        case "2":
            Dividing100ByANumber()
        case "3":
            MagicDate()
        case "4":
            LuckyTicket()
        case _:
            print("Введен неправильный номер.")
            TaskSelection()

###################################################
def GuessTheNumber():
    while 1 == 1:
        try:
            Number = int(input('Введите число: '))
            Result = Number % 3
        except ValueError:
            print('Введено не число!')
        else:
            if Result == 0 and Number != 0:
                print('Число', Number, 'делится на 3! ')
            elif Number == 0:
                print('Введён ноль!')
            else:
                print('Число', Number, 'не делится на 3!')
            break
###################################################

def DuplicateElements():
    while 1 == 1:
        try:
            Number = int(input('Введите число: '))
            Result = 100 / Number
        except ZeroDivisionError:
            print('Введён ноль!')
        except ValueError:
            print('Введено не число!')
        else:
            print('Результат деления 100 на введённое число: ', Result)
            break
###################################################

def DaysOff():
    while 1 == 1:
        date = input('Введите дату в формате дд.мм.гггг: ')
        try:
            valid_date = time.strptime(date, '%d.%m.%Y')
            date = date.split('.')
        except ValueError:
            print('Введена не дата!')
        else:
            if int(date[0]) * int(date[1]) == int(date[2][2:4]):
                print('Дата магическая!')
            else:
                print('Дата не является магической!')
            break

###################################################

def Students():
    while 1 == 1:
        try:
            TicketNumber = input('Введите номер билета: ')
            AmountLeft = 0
            AmountRight = 0
            if len(TicketNumber) % 2 == 0:
                for i in TicketNumber[0 : int(len(TicketNumber) / 2)]:
                    AmountLeft = AmountLeft + int(i)
                for i in TicketNumber[int(len(TicketNumber) / 2) : int(len(TicketNumber))+1]:
                    AmountRight = AmountRight + int(i)
                if AmountLeft == AmountRight:
                    print('Билет счастливый!')
                else:
                    print('Билет не является счастливым!')
                break
            else:
                print('Нечётное количество цифр!')
        except ValueError:
            print('Введено не число!')

###################################################

#Основная программа
TaskSelection()
