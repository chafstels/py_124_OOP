# '=======================================OOP================================'
# # OOP (Object-orientated-Programing - обьектно ориентированнное программирование) - это подход, при котором программа рассматривается как набор обьектов, взаимодействующих друг с другом
# # Парадигма - это совокупность идей и понятий, определяющий общий стиль написания кода(программы)
# # Класс - это некий шаблон для обьекта, который описывает все свойства и методы обьекта
# # Каждый обьект является экземпляром какого-то класса

# class Person:
#     # Атрибуты - переменные внутри класса
#     arms = 2
#     legs = 2
#     head = 1

#     # Методы - функции внутри класса
#     def __init__(self, name , age):
#         # __init__ - методы, который будет добавлять в обьект те атрибуты, которые отличаются у разных обьектов(экземпляров класса)
#         # self - cсылка на обьект, который только что создался
#         self.name = name
#         self.age = age

#     def walk(self):
#         print(f'{self.name} ходит')

#     def happy_brithday(self):
#         self.walk()
#         self.age += 1
#         print(f'{self.name}, c днем рождения! Вам исполнилось {self.age}')

# obj1 = Person('Maks', 23)
# obj2 = Person('Anton', 26)

# # print(obj1.arms)
# # print(obj2.arms)
# # print(obj1.name, obj1.age)
# # print(obj2.name, obj2.age)
# # obj1.walk()
# # obj2.walk()
# # obj1.happy_brithday()
# # obj1.happy_brithday()
# # print(obj1.age)


# '=================================Обьект класса============================='
# # Обьект, экземпляр, instance класса - сущность, созданная по шаблону класса (она принимает все атрибуты и методы класса)

# # Атрибут класса - переменная внутри класса
# # Атрибут экземпляра класса - переменная внутри класса созданная при обьявлении нового обьекта
# # Метод - функции внутри класса

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_age(self):
#         return f'Я {self.name} и мой возрасть {self.age}'

# animal1 = Animal('Cat', 3)
# animal2 = Animal('Dog', 5)
# animal3 = Animal('Bird', 2)

# print(animal1.get_age())
# print(animal2.get_age())
# print(animal3.get_age())


# class Phone:
#     def __init__(self, number, model):
#         self.number = number
#         self.model = model
#     def receive_call(self, name):
#         return f'Вам звонит {name}'
#     def get_number(self):
#         return self.number

# # phone1 = Phone('123-456-789', 'Iphone')
# # phone2 = Phone('999-221-332-441', 'Samsung')
# # print(phone1.receive_call('Anton'))
# # print(phone2.receive_call('Maks'))
# # print(phone1.get_number())
# # print(phone2.get_number())

# # class Laptop:
# #     def __init__(self, model):
# #         self.model = model
# #         self.memory = None
# #         self.screen_size = None
# #         self.ram = None
# #     def set_memory(self, memory):
# #         self.memory = memory
# #     def set_screen_size(self, size):
# #         self.screen_size = size
# #     def set_ram(self, ram):
# #         self.ram = ram
# #     def get_info(self):
# #         return f'Модель: {self.model}\nПамять: {self.memory}\nРазмер экрана: {self.screen_size}\nОперативная память: {self.ram}'
# # laptop = Laptop('Acer')
# # laptop.set_memory('512 GB SSD')
# # laptop.set_screen_size('15dm')
# # laptop.set_ram('16GB')
# # print(laptop.get_info())
# # laptop.set_memory('1TB SSD')
# # print(laptop.get_info())


# class Sniper:
#     health = 100
#     def __init__(self, name):
#         self.name = name

#     def shoot(self, sniper):
#         sniper.health -= 20
#         print(f'Атаковал {self.name}')
#         print(f'У {sniper.name} осталось {sniper.health}')

# sniper1 = Sniper('Aidana')
# sniper2 = Sniper('Ermek')
# import random
# while sniper1.health and sniper2.health:
#     choice = random.randint(1,2)
#     if choice == 1:
#         sniper1.shoot(sniper2)
#     else:
#         sniper2.shoot(sniper1)
# if sniper1.health:
#     print(f'{sniper1.name} - {sniper1.health} Победил!!!')
# else:
#     print(f'{sniper2.name} - {sniper2.health} Победил!!!')


# class Car:
#     def __init__(self, model, max_speed):
#         self.model = model
#         self.max_speed = max_speed
#     def upgrade(self):
#         self.max_speed += 1
#         return f'Максимальная скорость была увеличена до {self.max_speed}км\ч у автомобиля {self.model}'

# car1 = Car('BMW', 220)
# print(car1.upgrade())
# print(car1.max_speed)
# print(car1.upgrade())
# print(car1.upgrade())
# print(car1.upgrade())
# print(car1.upgrade())
# print(car1.max_speed)


# class Car:
#     model = 'Toyota'
#     speed = 0

#     def __init__(self, model, speed):
#         self.model = model
#         self.speed = speed

#     def upgrade(self):
#         self.speed += 1
#         # Car.speed +=1
#         print(f'{self.model} является моделью марки {Car.model}')
#         return (f'{self.model} имеет максимальную скорость {self.speed}')

# crown = Car('Crown', 240)
# print(crown.upgrade())
# print(crown.speed)


class Bank:
    balance = 0

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self):
        amount = int(input("Введите сумму которую желаете снять: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f'Вы сняли: {amount} и остаток вашего баланса: {self.balance}')
        else:
            print('Недостаточно стредств')

    def add_value(self):
        amount = int(input('Введите сумму пополнения: '))
        self.balance += amount
        print(f'Вы положили {amount} на счет и ваш баланс: {self.balance}')


    def main():
        bank = Bank(1_000_000)
        while True:
            choice = int(input('Выберите услугу:\n1: Пополнит счет\n2: Снять средства\n3: Проверить остаток счета\n4: Выход\n'))
            if choice == 1:
                bank.add_value()
            elif choice == 2:
                bank.withdraw()
            elif choice == 3:
                print(f'Your balance is {bank.balance}')
            elif choice == 4:
                break
            else:
                print('Не правильно ввели номер услуги')

Bank.main()
