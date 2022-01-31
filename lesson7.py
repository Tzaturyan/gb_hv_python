# Залдание №1

#a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
#b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

#class Matrix:
    #def __init__(self, lists):
        #self.lists = lists

    #def __str__(self):
        #return '\n'.join(map(str, self.lists))

    #def __add__(self, other):
        #c = []
        #for i in range(len(self.lists)):
            #c.append([])
            #for el in range(len(self.lists[0])):
                #c[i].append(self.lists[i][el] + other.lists[i][el])
        #return '\n'.join(map(str, c))

#matrix1 = Matrix(a)
#matrix2 = Matrix(b)

#print(matrix1, '\n')
#print(matrix2, '\n')
#print(matrix1 + matrix2)

# Задание №2

#from abc import ABC, abstractmethod

#class Clothes(ABC):
    #def __init__(self, param):
        #self.param = param

    #@property
    #@abstractmethod
    #def consumption(self):
        #pass

    #def __add__(self, other):
        #return self.consumption + other.consumption

#class Coat(Clothes):

    #@property
    #def consumption(self):
        #return round(self.param / 6.5) + 0.5

#class Costume(Clothes):
    #@property
    #def consumption(self):
        #return (2 * self.param + 0.3) / 100

#coat = Coat(58)
#costume = Costume(240)
#print(coat + costume)

# Задание №3

class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Рразмер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка уменьшилась, она равна: {sub} клеткам' if sub > 0 else 'Клетка исчезла'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '/n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell1 = Cell(26)
cell2 = Cell(4)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 / cell2)
print(cell1 * cell2)
print(cell1.make_order(5))

