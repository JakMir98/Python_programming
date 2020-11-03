#!/usr/bin/python
import matplotlib.pyplot as plt

x = [i for i in range(-100, 100)]

a = float(input('podaj wspolczynnik a fun'))
b = float(input('podaj wspolczynnik b fun'))
c = float(input('podaj wspolczynnik c fun'))

y1 = [a*i**2+b*i+c for i in x]
rozwiazania = []

delta = b**2-4*a*c
if delta > 0:
    rozwiazania.append((-b - delta**0.5)/(2*a))
    rozwiazania.append((-b + delta**0.5)/(2*a))
    print(rozwiazania)
elif delta == 0:
    rozwiazania.append((-b/(2*a)))
    print(rozwiazania)
else:
    print('Brak rozwiazan')

plt.plot(x, y1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcja kwadratowa')
plt.legend(('y(x)'))
plt.axis([-100, 100, -500, 5000])
plt.show()
