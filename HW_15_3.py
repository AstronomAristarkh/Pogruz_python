import sys
import logging
import argparse
import random


logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Животные')

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=int, nargs='*', help='press some numbers', default=[3])
args = parser.parse_args()


class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2
    
    def __str__(self):
        return f'{self.name} - {self.wing_length()}'

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'
    
    def __str__(self):
        return f'{self.name} - {self.depth()}'

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return 'Обычный'
    
    def __str__(self):
        return f'{self.name} - {self.category()}'

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            logger.critical('Пользователь промазал по клавиатуре')
            raise ValueError('Недопустимый тип животного')

zoopark = []
alfabet = 'abcdefghijklmnopqrstuvwxyz'
alfalist = list(alfabet)
logger.info(f'В зоопарк поступило {args.numbers[0]} животных')
for i in range(args.numbers[0]):
    random.shuffle(alfalist)
    name = ''.join([random.choice(alfalist) for x in range(random.randint(3,8))])
    zoopark.append(AnimalFactory.create_animal(random.choice(['Bird', 'Fish', 'Mammal']), name ,random.randrange(0,1001)))
    print(zoopark[i])
