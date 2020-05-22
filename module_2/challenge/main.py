from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary, departament):
        self.code = code
        self.name = name
        self.salary = salary
        self.__departament = departament

    @abstractmethod
    def calc_bonus(self):
        pass

    @staticmethod
    def get_hours():
        return 8

    def get_departament(self):
        return self.__departament.name

    def set_department(self, new_department, code):
        self.__departament = Department(new_department, code)


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 1))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, number_of_new_sales):
        self.__sales += number_of_new_sales

    def calc_bonus(self):
        number_of_sales = self.get_sales()
        return number_of_sales * 0.15
