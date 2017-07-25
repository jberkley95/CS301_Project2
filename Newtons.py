# John Berkley
# CS 301
# 7/24/2017

from fractions import Fraction
from sympy import *
x = symbols('x')
init_printing(use_unicode=True)

with open('/Users/johnberkley/PycharmProjects/CS301_Project2/input2.txt') as f:
    array = [[float(x) for x in line.split()] for line in f]

for i in range(1, len(array[0])):
    temp = [0 for x in range(len(array[0]) - i)]
    k = i
    for j in range(len(array[0]) - i):
        temp[j] = ((array[i][j+1] - array[i][j]) / (array[0][k] - array[0][j]))
        k += 1
    array.append(temp)

print('\nX'.ljust(10), end='')
for i in range(len(array[0])):
    print('F[', end='')
    for j in range(i):
        print(',', end='')
    print(']'.ljust(10), end='')
print()

for i in range(len(array[0])):
    j = 0
    while j < len(array[0]) + 1 - i:
        # Uncomment line 33 to display decimal values, and comment out 34
        # print('{0:.4f}'.format(array[j][i]).ljust(12), end='')
        print(str(Fraction(array[j][i]).limit_denominator()).ljust(12), end='')
        j += 1
    print()

polynomial = str(array[1][0])
for i in range(1, len(array[0])):
    polynomial += ' + (' + str(Fraction(array[i + 1][0]).limit_denominator()) + ')'
    for j in range(i):
        polynomial += '*(x - ' + str(Fraction(array[0][j]).limit_denominator()) + ')'

print('\nInterpolating polynomial is:\n')
print(polynomial)

print('\nSimplified polynomial is:\n')
print(simplify(eval(polynomial)))
