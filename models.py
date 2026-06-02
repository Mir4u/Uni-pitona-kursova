import math


class Calculator:
    def add(self, a, b):
        return f"{a} + {b} = {a + b}"

    def subtract(self, a, b):
        return f"{a} - {b} = {a - b}"

    def multiply(self, a, b):
        return f"{a} × {b} = {a * b}"

    def divide(self, a, b):
        if b == 0:
            return "Грешка: деление на нула"

        return f"{a} ÷ {b} = {a / b}"

    def power(self, a, b):
        result = a ** b

        if b == int(b) and b > 0:
            operation = " × ".join([str(a)] * int(b))
            return f"{a}^{int(b)} = {operation} = {result}"

        return f"{a}^{b} = {result}"

    def square_root(self, a):
        if a < 0:
            return "Грешка: отрицателно число"

        result = math.sqrt(a)
        return f"√{a} = {result}"

    def modulo(self, a, b):
        if b == 0:
            return "Грешка: деление на нула"

        return f"{a} % {b} = {a % b}"

    def floor_divide(self, a, b):
        if b == 0:
            return "Грешка: деление на нула"

        return f"{a} // {b} = {a // b}"

    def absolute(self, a):
        return f"|{a}| = {abs(a)}"

    def percentage(self, a, b):
        result = (a * b) / 100
        return f"{b}% от {a} = ({a} × {b}) ÷ 100 = {result}"

    def factorial(self, n):
        n = int(n)

        if n < 0:
            return "Грешка: отрицателно число"

        result = math.factorial(n)

        if n == 0:
            return "0! = 1"

        operation = " × ".join(str(i) for i in range(n, 0, -1))

        return f"{n}! = {operation} = {result}"