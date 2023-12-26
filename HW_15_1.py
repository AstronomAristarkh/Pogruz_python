import logging
import argparse


logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Матрицы')

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers',  default=[2, 2])
args = parser.parse_args()

class DifferentRangeError(Exception):
    pass

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [ [0]*self.cols for i in range(self.rows)]
        
    def __str__(self):
        stroka = ''
        for i in range(self.rows):
            for j in range(self.cols):
                stroka += str(self.data[i][j])
                if j < self.cols - 1:
                    stroka += ' '
            if i < self.rows - 1:
                stroka += '\n'
        return stroka
    
    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'
    
    def __eq__(self, other):
        equality = True
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.data[i][j] != other.data[i][j]:
                        equality = False
        else:
            equality = False
        return equality
    
    def __add__ (self, other):
        if self.rows == other.rows and self.cols == other.cols:
            summa = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    summa.data[i][j] = self.data[i][j] + other.data[i][j]
            return summa
        else:
            logger.critical('Чтобы сложить матрицы, они должны быть одинаковых размеров')
            raise DifferentRangeError ('Нельзя сложить матрицы разных размеров')
    def __mul__ (self, other):
        if self.cols == other.rows:
            proizvedenie = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        proizvedenie.data[i][j] += self.data[i][k] * other.data[k][j]
            logger.info('Фух, ну, вроде перемножили')
            return proizvedenie
        else:
            logger.critical('Чтобы перемножить матрицы, количество столбцов в первой матрице должно совпадать с количеством строк во второй')
            raise DifferentRangeError ('Нельзя перемножить матрицы разных размеров')
    
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [4, 5]]

matrix2 = Matrix(2, 2)
matrix2.data = [[7, 8], [10, 11]]
matrix3 = Matrix(int(args.numbers[0]), int(args.numbers[1]))
logger.info('Вот эта третья матрица, конечно, смысла не имеет, но, в зависимости от задачи, например единичную сюда подставить можно')
# Выводим матрицы
print(matrix1)

print(matrix2)
print(matrix1 == matrix2)
matrix_sum = matrix1 + matrix2 + matrix3
print(matrix_sum)
#matrix3 = Matrix(3, 2)
#matrix3.data = [[1, 2], [3, 4], [5, 6]]

#matrix4 = Matrix(2, 2)
#matrix4.data = [[7, 8], [9, 10]]

result = matrix1 * matrix2
print(result)
