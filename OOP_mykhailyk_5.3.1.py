import math

class Rational:
    def __reduce(self, a, b):
        k = math.gcd(a,b)
        self.a = a//k
        self.b = b//k

    def __init__(self, a, b=None):
        if isinstance(a, Rational):
            self.a=a.a
            self.b=a.b
        elif isinstance(a, int) and isinstance(b,int):
            if b == 0:
                raise ArithmeticError
            self.a = a
            self.b = b
        elif isinstance(a, str):
            if '/' in a:
                self.a, self.b = map(int, a.split("/"))
            else:
                self.a = int(a)
                self.b = 1

        self.__reduce(self.a, self.b)

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        if isinstance(other, Rational):
            nom = self.a*other.b + self.b*other.a
            den = self.b*other.b
        return Rational(nom, den)

    def __sub__(self, other):
        if isinstance(other, Rational):
            nom = self.a*other.b - self.b*other.a
            den = self.b*other.b
        return Rational(nom, den)

    def __mul__(self, other):
        if isinstance(other, Rational):
            nom = self.a*other.a
            den = self.b*other.b
            return Rational(nom, den)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            nom = self.a*other.b
            den = self.b*other.a
            return Rational(nom, den)

    def __call__(self):
        return self.a/self.b

    def __getitem__(self, key):
        if key == "n":
            return self.a
        elif key == "d":
            return self.b
        else:
            raise KeyError

def fileopen(filename):
    spisok = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data = line.split()
            result = Rational(0,1)
            operation = '+'
            for item in data:
                if item == '+':
                    operation = '+'

                elif item == '-':
                    operation = '-'

                elif item == '*':
                    operation = '*'

                else:
                    rat_num = Rational(item)


                    if operation == '+':
                        result += Rational(item)
                    elif operation == '-':
                        result -= Rational(item)
                    elif operation == '*':
                        result *= Rational(item)

                spisok.append(result)
    return spisok

def writefile(filename_output, sp):
    with open(filename_output, "w") as file:
        for item in sp:
            file.write()

if __name__ == '__main__':
    fileopen("input01.txt")
    writefile("output531.txt", spisok)

