class Human:
    def __init__(self, name = 'name', surname = 'surname', address = 'address', phone_number = 1):
        self.__name = name
        self.__surname = surname
        self.__address = address
        self.__phone_number = phone_number
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname
    
    def set_surname(self, surname):
        self.__surname = surname

    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address

    def get_phone_number(self):
        return self.__phone_number
    
    def set_phone_number(self, phone_number):
        try:
            int(phone_number)
            self.__phone_number = phone_number
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_phone_number(input('Введите номер телефона '))