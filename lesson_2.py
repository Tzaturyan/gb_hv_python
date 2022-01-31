# Задание №1

#my_tuple = (4, 'text', 352, 32.6, None)
#for i, item in enumerate(my_tuple, 1):
    #print(f"{i}) {item} - {type(item)}")

# Задание #2

#y_list = list(input("Введите числа без пробелов - "))

#for i in range(1, len(my_list), 2):
    #my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    #print(my_list)

# Задание №3

#month = int(input("Введите любой месяц от 1 до 12: "))
#month_dict = {
    #1: 'январь',
    #2: 'февраль',
    #3: 'март',
    #4: 'апрель',
    #5: 'май',
    #6: 'июнь',
    #7: 'июль',
    #8: 'август',
    #9: 'сентябрь',
    #10: 'октябрь',
    #11: 'ноябрь',
    #12: 'декабрь',
#}
#month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
              #'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#if month in month_dict:
    #print(f'{month}-й месяц года - это {month_dict[month]}')
    #print(f'{month}-й месяц года - это {month_list[month - 1]}')
#else:
    #print('Ошибка')

#while True:
    #user_month = input('Введите номер месяца от 1 до 12: ')
    #if user_month.isdigit() and 0 < int(user_month) <=12:
        #season_1 = ['зима', 'весна', 'лето', 'зима']
        #season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        #print(f'Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_2[int(user_month) // 3]}')
        #break
    #else:
        #print('Ошибка')

# Задание №4

# = input("Введите слово через пробелы - ").split()
#for i, word in enumerate(string, 1):
    #print(f'{i}) {word[:10]}')

# Задание №5

#my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
#new_number = int(input('Введите новый жлемент рейтинга в виде натурального числа - '))
#i = 0

#for n in my_list:
    #if new_number <= n:
        #i += 1

    #elif new_number > n:
        #break

#my_list.insert(i, float(new_number))
#print(my_list)

# Задание №6

goods = []
features = {'название': '', 'цена': '', 'колличество': '', 'единица изм': ''}
analytics = {'название': [], 'цена': [], 'колличество': [], 'единица изм': []}
num = 0

while True:
    if input('Для выхода из приложения нажмите Q, для продолжения Enter: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        prop = input(f'Введите значение свойства {f} - ')
        features[f] = int(prop) if (f == 'цена' or f == 'колличество') else prop
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\nТекущая аналитика по товарам:\n{'*' * 30}")
    for key, value in analytics.items():
        print(f"{key[:25]:>30}: {value}")
    print('*' * 30)


