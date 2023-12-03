class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience

class Driver(Person):
    def __init__(self, full_name, driving_experience):
        super().__init__(full_name, driving_experience)

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def __str__(self):
        return f"Марка: {self.brand}, Класс: {self.car_class}, " \
               f"Вес: {self.weight}, Водитель: {self.driver.full_name}, " \
               f"Мотор: {self.engine.power} от {self.engine.manufacturer}"

class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, payload_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return super().__str__() + f", Грузоподъемность: {self.payload_capacity}"

class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f", Предельная скорость: {self.max_speed}"

driver1 = Driver("Иванов Иван", 5)
engine1 = Engine("300 л.с.", "Manufacturer1")
car1 = Car("Toyota", "SUV", 1500, driver1, engine1)
print(car1)
car1.start()
car1.turn_left()
car1.stop()

lorry1 = Lorry("MAN", "Truck", 5000, driver1, engine1, 10000)
print(lorry1)
lorry1.start()
lorry1.turn_right()
lorry1.stop()

sportcar1 = SportCar("Ferrari", "Sport", 1200, driver1, engine1, "350 км/ч")
print(sportcar1)
sportcar1.start()
sportcar1.turn_right()
sportcar1.stop()
