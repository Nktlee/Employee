from human import Human
from product import Product

class Employee(Human):
    def __init__(self, employee_number = 123, qualification = 'worker'):
        self.__employee_number = employee_number
        self.__qualification = qualification

    def get_employee_number(self):
        return self.__employee_number
    
    def set_employee_number(self, employee_number):
        try:
            int(employee_number)
            self.__employee_number = employee_number
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_employee_number(input('Введите номер сотрудника '))
    
    def get_qualification(self):
        return self.__qualification

    def set_qualification(self, qualification):
        try:
            qualification = int(qualification)
            qualification_dict = {1 : "новичок", 2 : "средний работник", 3 : "профессионал"}
            if qualification in qualification_dict:
                self.__qualification = qualification_dict[qualification]
            else:
                raise ValueError
        except ValueError:
            print('Ошибка: введите уровень квалификации (1 - новичек, 2 - средний работник, 3 - профессионал)')
            self.set_qualification(input('Введите уровень квалификации (1 - новичек, 2 - средний работник, 3 - профессионал) '))

    def create_product(self, product: Product, human: Human):
        qualification_dict = {"новичок" : 1, "средний работник" : 2, "профессионал" : 3}
        time = product.get_coefficient() * 30 / qualification_dict[self.get_qualification()]
        print(f'{human.get_name()} создаст продукт {product.get_title()} за {time} минут')