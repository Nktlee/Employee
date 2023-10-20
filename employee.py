from human import Human

class Employee(Human):
    def __init__(self, name = 'name', surname = 'surname', address = 'address', phone_number = 1, employee_number = 123, qualification = 'worker'):
        super().__init__(name, surname, address, phone_number)
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
            if qualification == 1:
                self.__qualification = "новичок"
            elif qualification == 2:
                self.__qualification = "средний работник"
            elif qualification == 3:
                self.__qualification = "профессионал"
            else:
                print('Ошибка: введите уровень квалификации (1 - новичек, 2 - средний работник, 3 - профессионал)')
                self.set_qualification(input('Введите уровень квалификации '))
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_qualification(input('Введите уровень квалификации '))