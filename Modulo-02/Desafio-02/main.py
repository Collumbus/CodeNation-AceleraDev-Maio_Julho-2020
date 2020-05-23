import abc

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee(abc.ABC):

    @abc.abstractmethod
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8
        self._departament = Department(self.name, self.code)

    @abc.abstractmethod
    def calc_bonus(self):
        pass
    
    def get_hours(self):
        return self.hours

    def get_department(self):
        return self._departament.name

    def set_department(self, departament):
        self._departament.name = departament

class Manager(Employee):
    def __init__(self, code, name, salary, ):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, sale):
        self._sales += sale

    def calc_bonus(self):
        return self._sales * 0.15

if __name__ == '__main__':

    t1 = Manager('0001', 'Marco', 5000)
    print(t1.get_department())
    t1.set_department('sellers')
    print(t1.get_department())
    