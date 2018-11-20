import math
while True:
    print("""Выбирите нужную операцию:
            1) Найти сумму цифр и количество цифр заданного натурального числа.
            2) Возвести число в натуральную степень n.
            3) Найти количество различных цифр у заданного натурального числа.
            4) Найти наибольшую цифру натурального числа.
            5) Задано натуральное число. Проверить, является ли заданое натуральное число палиндромом.
            6) Определить является ли заданное натуральное число простым.
            7) Найти все все простые делители заданного натурльного числа.
            8) Найти НОД и НОК двух натурльных чисел.
            9) Заданы три целых числа , которыю задают некоторую дату.\n                Определить дату следующего дня.
            10) Запрограммировать последовательность чисел Фибоначчи\n                (пользователь вводит порядковый номер элемента \n                 последовательности Фибоначчи,а программа выводит на экран его значение.
            0) Введите 0 чтобы покинуть программу.\n
            """)
    try:
        choice = int(input())
    except ValueError:
        choice = 11
    if choice == 1:
        print("Выбран 1ый пункт меню.")
        number_1 = input("Введите ваше число: ")
        summa = 0
        amount = 0
        for i in number_1:
            summa += int(i)
            amount += 1
        print("Сумма чисел =",summa,".\nКоличесвто цифр = ",amount,".")
    elif choice == 2:
        print("Выбран 2ой пункт меню.")
        number_2 = int(input("Введите ваше число: "))
        p = int(input("Введите натуральную степень n: "))
        res = pow(number_2,p)
        print("Итоговое число = ",res,".")
    elif choice == 3:
        print("Выбран 3ий пункт меню.")
        amount_3 = 0
        number_3 = set(input("Введите ваше число:"))
        for i in number_3:
            amount_3 += 1
        print("Количество разных цифр в числе = ",amount_3,".")
    elif choice == 4:
        print("Выбран 4ый пункт меню.")
        number_4 = int(input("Введите ваше число: "))
        maximal = number_4%10
        number_4 = number_4//10
        while number_4 > 0:
            if number_4 % 10 > maximal:
                maximal = number_4 % 10
            number_4 = number_4//10
        print("Максимум =",maximal)
    elif choice == 5:
        print("Выбран 5ый пункт меню.")
        number_5 = input("Введитее ваше число: ")
        l_of_number = len(number_5)
        for i in range(l_of_number//2):
            if number_5[i] != number_5[-1-i]:
                print("Число не палиндром.")
                break
        else:
            print("Число палиндром.")
    elif choice == 6:
        print("Выбран 6ой пункт меню.")
        number_6 = int(input("Введите ваше число: "))
        max_divider = int(number_6//2)
        for i in range(2,max_divider+1):
            if number_6%max_divider == 0:
                print(max_divider , "- делитель")
                print("Число имеет более 3-х делителей из них: ",number_6,", 1, ",max_divider,".")
                break
            else:
                max_divider -= 1
        else:
            print("Число простое.")
    elif choice == 7:
        print("Выбран 7ой пункт меню.")
        number_7 = int(input("Введите ваше число: "))
        divider = 0
        for i in range(1,number_7):
            if number_7%i == 0:
                for n in range(2,i-1):
                    if i/n == 0:
                        print("Делитель ",i,"составной.")
                    else:
                        print(i,"- простой делитель.")
                        divider += 1
            else:
                continue
        print("У заданного числа ",divider,"простых делителей.")
    elif choice == 8:
        print("Выбран 8ой пункт меню.")
        a = int(input("Введите 1ое число: "))
        b = int(input("Введите 2ое число: "))
        def FIND_NOD(a,b):
            while a != 0 and b != 0 :
                if a > b:
                    a = a%b
                else:
                    b = b%a
            return a+b
        print("НОД = ",FIND_NOD(a,b),".")
        print("НОК = """,(a*b)/FIND_NOD(a,b),".")
    elif choice == 9:
        print("Выбран 9ый пункт меню.")
        print("Программа в разработке.")
    elif choice == 10:
        print("Выбран 10ый пункт меню.")
        amount_10 = int(input("Введите порядковый номер числа Фибоначчи: "))
        number_10_1 = 1
        number_10_2 = 1
        print(number_10_1,number_10_2,end=" ")
        for i in range (3,amount_10+1):
            print(number_10_1+number_10_2,end=" ")
            b = number_10_1
            number_10_1 = number_10_2
            number_10_2 = b + number_10_1
    elif choice == 0:
        print("До скорой встречи.")
        break
    else:
        print("Введен некоректный пункт меню.")