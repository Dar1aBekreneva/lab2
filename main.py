def q1():
     n = str(input("Введите пароль"))
     m = str(input("Введите пароль"))
     if n!= m:
          print("Пароль неверный")
     else:
          print("Пароль верный!")

def q2():
     n = int(input("Введите номер места: "))
     if n > 36:
          print("Плацкарт")
     else:
          print("Купе")
     if n % 2==0:
          print("Верхнее место")
     else:
          print("Нижнее место")

def q3():
     n = int(input("Введите год: "))
     if n % 4 == 0 and (n % 100) % 4 == 0:
          print ("Год високосный")
     else:
          print ("Год не високосный")

def q4():
    colors = ('красный', 'синий', 'желтый')
    c1 = input()
    c2 = input()
    if c1 in colors and c2 in colors:
        if c1 != c2:
            if (c1 in ('красный', 'синий')) and (c2 in ('красный', 'синий')):
                print('фиолетовый')
            if (c1 in ('красный', 'желтый')) and (c2 in ('красный', 'желтый')):
                print('оранжевый')
            if (c1 in ('синий', 'желтый')) and (c2 in ('синий', 'желтый')):
                print('зеленый')
        else:
            print(c1)
    else:
        print("ошибка цвета")

q1()
