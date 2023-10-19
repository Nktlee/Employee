from employee import Employee

class Boss(Employee):
    def __init__(self, employee_number = 123, annual_salary = 1, bonus = 1):
        super().__init__(employee_number)
        self.__annual_salary = annual_salary
        self.__bonus = bonus

    def get_annual_salary(self):
        return self.__annual_salary
    
    def set_annual_salary(self, annual_salary):
        try:
            int(annual_salary)
            self.__annual_salary = annual_salary
        except ValueError:
            print('Ошибка: введите целое число ')
            self.set_annual_salary(input('Введите годовой оклад '))
    
    def get_bonus(self):
        return self.__bonus
    
    def set_bonus(self, bonus):
        try:
            int(bonus)
            self.__bonus = bonus
        except ValueError:
            print('Ошибка: введите целое число ')
            self.set_bonus(input('Введите годовой оклад '))