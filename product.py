class Product:
    def __init__(self, title = 'title', width = 1, length = 1, height = 1, weight = 1, coefficient = 1):
        self.__title = title
        self.__width = width
        self.__length = length
        self.__height = height
        self.__weight = weight
        self.__coefficient = coefficient

    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        try:
            int(width)
            self.__width = width
        except ValueError:
            print('Ошибка: введите целое число ')
            self.set_width(input('Введите ширину '))

    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        try:
            int(length)
            self.__length = length
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_length(input('Введите длину '))

    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        try:
            int(height)
            self.__height = height
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_height(input('Введите высоту '))

    def get_weight(self):
        return self.__weight
    
    def set_weight(self, weight):
        try:
            int(weight)
            self.__weight = weight
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_weight(input('Введите вес '))

    def get_coefficient(self):
        return self.__coefficient
    
    def set_coefficient(self, coefficient):
        try:
            coefficient = int(coefficient)
            if coefficient == 1:
                self.__coefficient = "легко"
            elif coefficient == 2:
                self.__coefficient = "средне"
            elif coefficient == 3:
                self.__coefficient = "сложно"
            else:
                print('Ошибка: введите сложность производства (1 - легко, 2 - средне, 3 - сложно)')
                self.set_coefficient(input('Введите сложность производства '))
        except ValueError:
            print('Ошибка: введите целое число')
            self.set_coefficient(input('Введите сложность производства '))
        