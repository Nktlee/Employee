from employee import Employee

class Carpenter(Employee):
    def __init__(self, shift_number = 1, hourly_wage = 1000):
        self.__shift_number = shift_number
        self.__hourly_wage = hourly_wage
    
    def get_shift_number(self):
        if self.__shift_number == 1:
            return 'Дневная смена'
        else:
            return 'Ночная смена'
    
    def set_shift_number(self, shift_number):
        try:
            shift_number = int(shift_number)
            if shift_number == 1 or shift_number == 2:
                self.__shift_number = shift_number
            else:
                print('Ошибка: введите номер смены (1 - дневная, 2 - ночная)')
                self.set_shift_number(input('Введите номер смены (1 - дневная, 2 - ночная) '))
        except ValueError:
            print('Ошибка: введите целое число ')
            self.set_shift_number(input('Введите номер смены (1 - дневная, 2 - ночная) '))

    def get_hourly_wage(self):
        return self.__hourly_wage
    
    def set_hourly_wage(self, hourly_wage):
        try:
            int(hourly_wage)
            self.__hourly_wage = hourly_wage
        except ValueError:
            print('Ошибка: введите целое число ')
            self.set_hourly_wage(input('Введите почасовую оплату '))