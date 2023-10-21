from carpenter import Carpenter
from boss import Boss
from product import Product

chel = Carpenter()

product = Product(coefficient=1)

# setter
# human
chel.set_name(input('Введите имя '))
chel.set_surname(input('Введите фамилию '))
chel.set_address(input('Введите адрес '))
chel.set_phone_number(input('Введите номер телефона '))

# carpenter
chel.set_shift_number(input('Введите номер смены '))
chel.set_hourly_wage(input('Введите почасовую оплату '))

# employee
chel.set_employee_number(input('Введите номер сотрудника '))
chel.set_qualification(input('Введите уровень квалификации '))

# product
product.set_name(input('Введите название продукта '))
product.set_width(input('Введите ширину продукта '))
product.set_length(input('Введите длину продукта '))
product.set_height(input('Введите высоту продукта '))
product.set_weight(input('Введите вес продукта '))

# getter
# human
print('Имя:', chel.get_name())
print('Фамилия:', chel.get_surname())
print('Адрес:', chel.get_address())
print('Номер телефона:', chel.get_phone_number())
print()

# carpenter
print(chel.get_shift_number())
print('Ставка:', chel.get_hourly_wage())
print()

# employee
print('Номер сотрудника:', chel.get_employee_number())
print('Квалификация:', chel.get_qualification())
print()

# product
print('Название продукта:', product.get_name())
print('Ширина:', product.get_width())
print('Длина:', product.get_length())
print('Высота:', product.get_height())
print('Вес:', product.get_weight())