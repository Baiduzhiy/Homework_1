class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"{self.number}"

    def __add__(self, other):
        return self.number + other.number


complex_1 = ComplexNumber(2 + 3j)
complex_2 = ComplexNumber(3 + 2j)
print(complex_1)
print(complex_2)

print(complex_1 + complex_2)