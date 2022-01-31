# Задание №1

#value_1 = 'hello'
#value_2 = 'world'
#print(f"{value_1}, {value_2}")
#num_1 = int(input('Введите число: '))
#num_2 = int(input('Введите число: '))
#print(f"Вы ввели числа {num_1} и {num_2}")
#word = input("Введите строку: ")
#print(f"{word}-отличный выбор!")

# Задание №2
#time = int(input("Введите время в секундах - "))
#hours = time // 3600
#minutes = (time // 60)-(hours * 60)
#seconds = time % 60
#print(f"{hours:02}:{minutes:02}:{seconds:02}")

# Задание №3

#number = input("Введите положительное число - ")

#while int(number) < 0:
    #print('Я же сказал, положительное!')
    #number = input("Введите пооложительное число - ")

#print(f"{number} + {number + number} + {number + number + number}) = "
      #f"{int(number) + int(number + number) + int(number + number + number)}")

# Задание №4

#num_init = int(input('Введите целое положительное число - '))
#maximum = num_init % 10
#num = num_init

#while num > 0:
    #digit = num % 10
    #if digit > maximum:
        #maximum = digit
    #if digit == 9:
        #break
    #num = num //= 10
    #print(num)
#print(f"Наибольшая цифра в числе {num_init} равна {maximum}")

#Задание №5

#revenue = float(input("Введите значение выручки - "))
#costs = float(input("Введите значение издержек - "))
#result = revenue - costs
#if result > 0:
    #print(f"Поздравляю! Ваша компания работает с прибылью {result} !")
    #print(f"Рентабельность выручки - {result / revenue:.3f}")
    #persons = int(input("Сколько сотрудников работает в вашей компании? - "))
    #print(f"прибыль на одного сотрудника - {result / persons:.3f}")
#elif result < 0:
    #print(f"Вы работаете с убытков {-result}")
#else:
    #prunt(f"Ноль - это тоже хороший результат! Зато стабильно!")

# Задание №6

#while True:
    #days = 1
    #start_km = float(input('Начальный результат - '))
    #last_km = float(input('Финальный результат - '))
    #if start_km <= 0 or last_km < 0:
        #print('Результат должен быть больше нуля!')
    #else:
        #while start_km < last_km:
            #start_km *= 1.1
            #days += 1
        #print(f'Спортсмен добьётся результата за {days} дней')



