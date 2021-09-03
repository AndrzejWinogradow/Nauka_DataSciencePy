#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab
print('wydruk funkcji y = a*x*x + bx + c')
a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
c = int(input('Podaj współczynnik c: '))
x = range(-10, 11)  # lista argumentów x

y = []  # lista wartości
for i in x:
    y.append(a * i * i + b * i + c)

pylab.plot(x, y)
pylab.title('Wykres f(x) = y = a*x*x + bx + c')
pylab.grid(True)
pylab.show()