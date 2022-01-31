# Задание №1

#with open('first.txt', 'w', encoding='utf-8') as f:
    #while True:
        #line = input('Введите новую строку - ')
        #if not line:
            #break
        #f.write(f'{line}\n')

# Задание №2

#with open('second.txt', 'r', encoding='utf-8') as f:
    #userfile = [f'{num}. {" ".join(line.split())} - {len(line.split())} слов ' for num, line in enumerate(f, 1)]
    #print(*userfile, f'всего строк - {len(userfile)}.', sep='\n')

# Задание №3

#with open('fird.txt', 'r', encoding='utf-8') as f:
    #employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    #print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          #f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

# Задание №4

#rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
#with open('four.txt', 'w', encoding='utf-8') as nf:
    #with open('four2.txt', 'r', encoding='utf-8') as mf:
        #nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in mf]))

# Задание №5

#from random import randint
#with open('five.txt', mode='w+', encoding='utf-8') as f:
    #f.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    #f.seek(0)
    #print(sum(map(int, f.readline().split())))

# Задание №6

#mydict = {}
#with open("six.txt", encoding='utf-8') as f:
    #for line in f:
        #name, stats = line.split(':')
        #elems = [i for i in stats if i == ' ' or (i >= '0' and i <= '9')]
        #name_sum = sum(map(int, "".join(elems).split()))
        #mydict[name] = name_sum
#print(f"{mydict}")

# Задание №7

import json

with open('seven.json', 'w') as fw:
    with open('seven.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) >0]) /
                                                     len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, fw, ensure_ascii=False, indent=4)




