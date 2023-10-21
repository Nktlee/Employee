from carpenter import Carpenter
from product import Product
from human import Human

human = Human(address='moscow')
chel = Carpenter()
product = Product(coefficient=1)

# setter
# human
chel.set_name(input('Введите имя '))
chel.set_surname(input('Введите фамилию '))
chel.set_address(input('Введите адрес '))
chel.set_phone_number(input('Введите номер телефона '))

# carpenter
chel.set_shift_number(input('Введите номер смены (1 - дневная, 2 - ночная) '))
chel.set_hourly_wage(input('Введите почасовую оплату '))

# employee
chel.set_employee_number(input('Введите номер сотрудника '))
chel.set_qualification(input('Введите уровень квалификации (1 - новичек, 2 - средний работник, 3 - профессионал) '))

# product
product.set_title(input('Введите название продукта '))
product.set_width(input('Введите ширину продукта '))
product.set_length(input('Введите длину продукта '))
product.set_height(input('Введите высоту продукта '))
product.set_weight(input('Введите вес продукта '))

# getter
# human
print('-------------------------')
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
print('Название продукта:', product.get_title())
print('Ширина:', product.get_width())
print('Длина:', product.get_length())
print('Высота:', product.get_height())
print('Вес:', product.get_weight())
print()

# calculate time of the creating product
chel.create_product(product, human)