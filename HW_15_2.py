# Введите ваше решение ниже
import logging
import argparse
import random


logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Прямоугольники')

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers',  default=[5])
args = parser.parse_args()

class NegativeValueError(Exception):
    
    pass
    
class Rectangle:

    def __init__(self, width, height=None):
       
        self.width = width
        if height is None:
            self.height = width
            
        else:
            self.height = height
        if self.width < 0:
            logger.critical('Отрицательные длины - это чёт совсем неевклидовое.')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {self.width}')
        if self.height < 0:
            logger.critical('Отрицательные длины - это чёт совсем неевклидовое.')
            raise NegativeValueError(f'Высота должна быть положительной, а не {self.height}')
        if self.height == self.width:
            logger.info('Получился квадрат')
    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        
        return self.width * self.height

    def __add__(self, other):
        
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
       
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        
        return self.area() < other.area()

    def __eq__(self, other):
        
        return self.area() == other.area()

    def __le__(self, other):
        
        return self.area() <= other.area()

    def __str__(self):
        
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        
        return f"Rectangle({self.width}, {self.height})"


rectangles = []    
for i in range(int(args.numbers[0])):
    rectangles.append(Rectangle(random.randint(-1, 10), random.randint(1, 10)))
    print(rectangles[i])
print(rectangles)