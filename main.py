from employee import Employee
from carpenter import Carpenter
from boss import Boss

chel = Carpenter()

chel.set_name(input('Введите имя '))
chel.set_employee_number(input('Введите номер сотрудника '))
chel.set_shift_number(input('Введите номер смены '))
chel.set_hourly_wage(input('Введите почасовую оплату '))

print('Имя: ', chel.get_name())
print('Номер сотрудника: ', chel.get_employee_number())
print(chel.get_shift_number())
print('Ставка: ', chel.get_hourly_wage())