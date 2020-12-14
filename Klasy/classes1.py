#!/usr/bin/python

import math as m


class Complex:
    """Class represent complex number"""

    def __init__(self, real=0, imag=0):
        self.re = real
        self.im = imag

    def conjugate(self):
        self.im = -self.im

    def abs(self):
        return m.sqrt(self.im * self.im + self.re * self.re)

    # overload +
    def __add__(self, o):
        c = Complex(self.re + o.re, self.im + o.im)
        return c

    # overload -
    def __sub__(self, o):
        c = Complex(self.re - o.re, self.im - o.im)
        return c

    # overload *
    def __mul__(self, o):
        c = Complex(self.re*o.re - self.im*o.im, self.re*o.im + self.im*o.re)
        return c

    # overload /
    def __truediv__(self, o):
        div = self.re * o.re + o.im * o.im
        if div == 0:
            return

        re = self.re * o.re + self.im * o.im
        re = re/div

        im = self.im * o.re - self.re * o.im
        im = im/div

        c = Complex(re, im)

        return c

    # overload str()
    def __str__(self):
        return "({:.2f}, j{:.2f})".format(self.re, self.im)

    # overload ==
    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    # overload !=
    def __ne__(self, o):
        return self.re != o.re and self.im != o.im or self.re != o.re or self.im != o.im

    # overload <
    def __lt__(self, o):
        self_mag = math.sqrt((self.x ** 2) + (self.y ** 2))
        other_mag = math.sqrt((o.x ** 2) + (o.y ** 2))
        return self_mag < other_mag

    # overload >
    def __gt__(self, o):
        self_mag = math.sqrt((self.x ** 2) + (self.y ** 2))
        other_mag = math.sqrt((o.x ** 2) + (o.y ** 2))
        return self_mag > other_mag
