'=================================Полиморфизм=========================='
# Полиморфизм - это принцип ООП, в котором в разных классах методы называются одинаково, но имеют разный функционал(другая логика реализации кода)
# Преимущества полиморфизма:
# Код не зависит от типов обьекта, что делает его более гибким и пригодным для повторного использования
# Код становится более читаемым, так как методы с одинаковым названием выполняют логически похожие действия, но с учетом специфики разных типов

class Dog:
    def speak(self):
        print('GAV GAV')
class Cat:
    def speak(self):
        print('Mew-Mew')
class Fish:
    def speak(self):
        print('OP-OP')

objects = [Dog(), Cat(), Fish()]
for obj in objects:
    obj.speak()


"""
1) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""

# class Numberbook:
#     def __init__(self, name, last_name, number):
#         self.name = name
#         self.last_name = last_name
#         self.number = number
#     def get_info(self):
#         print(f'контакт:{self.name} {self.last_name}, телеон:{self.number}')
# information = Numberbook('Tilek', 'Duishenbekov', +996551693666)
# information.get_info()

'''
Дан словарь:
a = {1: 'OOP basics', 2: 'Inheritance', 3: 'Polymorphism', 4: 'Encapsulation'}.

Создайте класс PythonCourse, параметр экземляра которого принимает словарь a. Добавьте в класс функцию learn, которая добавляет в этот словарь новый элемент. Создайте объект от PythonCourse, вызовите функцию learn и распечатайте сам объект.
Например, если добавить элемент с ключом 5 и значением ‘Abstraction’, на выходе мы получим:
{1: 'OOP basics', 2: 'Inheritance', 3: 'Polymorphism', 4: 'Encapsulation', 5: 'Abstraction'}
# '''
# class PythonCourse:
#     def __init__(self, course_theme):
#         self.course_theme = course_theme
#     def learn(self, course_name):
#         for key, value in course_name.items():
#             self.course_theme[key]=value
#             return self.course_theme

# course_theme = {1: 'OOP basics', 2: 'Inheritance', 3: 'Polymorphism', 4: 'Encapsulation'}
# new_dict = PythonCourse(course_theme)
# print(new_dict.learn({5:'Abstraction'}))

'=============================Естественные примеры полиморфизма==================='
# Operator +
num1 = 1
num2 = 2
print(num1 + num2)
str1 = '1'
str2 = '2'
print(str1 + str2)

# Len
print(len('Python'))
print(len(['python', 'java', 'C']))
print(len({'name': 'Anton', 'age':25}))
