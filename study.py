# ЗАДАНИЕ 1 — Наследование
# Создай класс Person с name и age, от него наследуй Student с grade
class Person:
    name = None
    age = None
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def get_info(self):
        print("Name", self.name, "Age", self.age)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_info(self):
        super().get_info()
        print("Grade", self.grade)

s1 = Student("Damir", 17, 11) 
s1.get_info()

# ЗАДАНИЕ 2 — Полиморфизм
# Базовый класс Device, подклассы Laptop и Smartphone переопределяют turn_on
class Device:
    model = None
    def __init__(self, model):
        self.model = model
    
    def turn_on(self):
        print("Model", self.model)

class Laptop(Device):
    def turn_on(self):
        print("New model", self.model)

class Smartphone(Device):
    def __init__(self, model, memory):
        super().__init__(model)
        self.memory = memory
    
    def turn_on(self):
        super().turn_on()
        print("Memory", self.memory)

l1 = Laptop("ASUS ROG Zephyrus G14")
l1.turn_on()

s1 = Smartphone("Mi 10", 256)
s1.turn_on()



# ЗАДАНИЕ 3 — Инкапсуляция + Наследование
# Базовый класс BankAccount с приватным полем __balance
# SavingsAccount наследует и добавляет метод add_interest

class BankAccount:
    __balance = 0

    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        print("Balance:", self.__balance)

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient funds")
        else:
            self.__balance -= amount

b = BankAccount(10000)
b.deposit(100)
b.get_balance()
b.withdraw(100000)
b.get_balance()
b.withdraw(5100)
b.get_balance()


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:  # Проверяем, что ставка положительная
            interest = self._BankAccount__balance * (rate / 100)  # Вычисляем проценты
            self.deposit(interest)  # Добавляем проценты к балансу
            print(f"Added interest: {interest}")
        else:
            print("Interest rate must be positive!")

savings = SavingsAccount(10000)
savings.add_interest(5) # Добавит 5% на остаток
savings.get_balance()  






# Код записанный с видеоурока:

# class Building:
#     __year = None
#     __city = None
    
#     def __init__(self,year,city):
#         self.year = year
#         self.city = city
    
#     def get_info(self):
#         print("Year",self.year,"City",self.city)


# class School(Building):
#     pupils = 0

#     def __init__(self,pupils, year, city):
#         super(School,self).__init__(year,city)
#         self.pupils = pupils
        

#     def get_info(self):
#         super().get_info()
#         print("Pupils",self.pupils)
# class House(Building):
#     pass

# class Shop(Building):
#     pass
# school = School(100,1000,"Moscow")
# school.get_info()
# house = House(1000,"Astana")
# house.get_info()
# shop = Shop(1000,"Moscow")
# shop.get_info()
