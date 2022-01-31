# Задание №1

#def div(s_1, s_2):
    #try:
        #s_1, s_2 = int(s_1), int(s_2)
        #div_num = s_1 // s_2
    #except ValueError:
        #return 'Некорректные данные'
    #except ZeroDivisionError:
        #return 'Делить на ноль нельзя'
    #return round(div_num, 4)

#print(div(input('Введите первое число - '), input('Введите второе число - ')))

# Задание №2

#def person_inf(name, surname, birthday, city, email, phone):
    #return f"Name - {name}; Surname - {surname}; Birthday - {birthday}; City - {city};\"" \
           #f"Email - {email}; Phone - {phone};"

#name = input('Введите имя - ')
#surname = input('Введите фамилию - ')
#birthday = input('Когда день рождение - ')
#city = input('Введите город - ')
#email = input('Введите email - ')
#phone = input('Введите phone - ')

#print(person_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))

# Задание №3

#def my_func(arg1, arg2, arg3):
    #my_list = [arg1, arg2, arg3]
    #return sum(sorted(my_list)[1:])
#print(my_func(2, 11, -30))

#Задание №4

#def my_pow_fun(x,y):
    #try:
        #x,y = float(x), int(y)
        #if x <= 0 or y >=0:
            #return 'Ошибка x должен быть больше 0, а y должен быть меньше 0'
        #else:
            #result = 1
            #for _ in range(abs(y)):
                #result *= 1/x
            #return f'результат возведения x в степень y:{round(result, 6)}'
    #except ValueError:
        #return "Программа работает только с числами"
#print(my_pow_fun(2,-3))

#Задание №5

#def sum_num():
    #s = 0
    #while True:
        #in_list = input('Введите число или Q для выхода: ').split()
        #for num in in_list:
            #if num == 'q':
                #return s
            #else:
                #try:
                    #s += int(num)
                #except ValueError:
                    #print('Чтобы выйти из программы нажмите q - ')
            #print(f'Сумма чисел = {s}')

#num = 0
#try:
    #while num != 'q':
        #for i in map(int, input('Для выхода наберите q Введите числа используя пробел - ').split()):
            #num += i
            #print(num)
#except ValueError:
    #print(num)

# Задание #6

def int_func(word):
    latin_char = 'gjhghjg'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Введите строку из слов разделенных пробелами').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')