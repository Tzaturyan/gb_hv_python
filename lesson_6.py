# Задание №1

#import time
#import itertools

#class TrafficLight:
    #__color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7,32]], ["yellow", [2, 33]]]
    #def running(self):
        #for light in itertools.cycle(self.__color):
            #print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            #time.sleep(light[1][0])

#trf = TrafficLight()
#trf.running()

# Задание №2

#class Road:

    #def __init__(self, length, width):
        #self._length = length
        #self._width = width

    #def get_full_profit(self):
        #return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"

#road_1 = Road(6000, 16)
#print(road_1.get_full_profit())

# Зададние №3

#class Worker:
    #def __init__(self, name, surname, position, wage, bonus):
        #self.name =name
        #self.surname = surname
        #self.position = position
        #self._income = {'profit': wage, 'bonus': bonus}

#class Position(Worker):
    #def get_full_name(self):
        #return f"{self.name} {self.surname}"
    #def get_full_profit(self):
        #return f"{sum(self._income.values())}"

#manager = Position("Andrey", "Ivanov", "CEO", 25000, 10000)
#print(manager.get_full_name())
#print(manager.position)
#print(manager.get_full_profit())

# Задание №4

#class Car:

    #def __init__(self, name, color, speed, is_police=False):
        #self.name = name
        #self.color = color
        #self.speed = speed
        #self.is_police = is_police
        #print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")

    #def go(self):
        #print(f"{self.name}: Машина поехала")

    #def stop(self):
        #print(f"{self.name}: Машина остановилась")

    #def turn(self, direction):
        #print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}")

    #def show_speed(self):
        #print(f"{self.name}: Скорость автомобиля - {self.speed}")

#class WorkCar(Car):
    #def __init__(self, name, color, speed, is_police=False):
        #super().__init__(name, color, speed, is_police)

    #def show_speed(self):
        #return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!" \
            #if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}"

#work_car = WorkCar('Автобус', 'Синий', 42)
#print (work_car.show_speed())

#class PoliceCar(Car):
    #def __init__(self, name, color, speed, is_police=True):
        #super().__init__(name, color, speed, is_police)

#police_car = PoliceCar('ДПС', 'Чёрный', 80)
#police_car.go()


#class SportCar(Car):
    #"""Спортивный автомобиль"""

#class TownCar(Car):
    #def __init__(self, name, color, speed, is_police=False):
        #super().__init__(name, color, speed, is_police)

    #def show_speed(self):
        #return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!" \
            #if self.speed > 80 else f"{self.name}: Скорость автомобиля - {self.speed}"

#town_car = TownCar('Феррари', 'Белый', 82)
#print (town_car.show_speed())

# Задание №5

class Stationary:

    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f'Just start drawing! {self.title}')

class Pen(Stationary):
    def draw(self):
        print(f'Just start drawing with Pen! {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Just start drawing with Pencil! {self.title}')

class Marker(Stationary):
    def draw(self):
        print(f'Just start drawing with Marker! {self.title}')

stat = Stationary()
mark = Marker()
pen = Pencil()

stat.draw()
mark.draw()
pen.draw()








