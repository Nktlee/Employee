from human import Human

class Employee(Human):
    def __init__(self, name = 'name', surname = 'surname', address = 'address', phone_number = 1, employee_number = 123):
        super().__init__(name, surname, address, phone_number)
        self.__employee_number = employee_number

    def get_employee_number(self):
        return self.__employee_number
    
    def set_employee_number(self, employee_number):
        try:
            int(employee_number)
            self.__employee_number = employee_number
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_employee_number(input('Введите номер сотрудника '))