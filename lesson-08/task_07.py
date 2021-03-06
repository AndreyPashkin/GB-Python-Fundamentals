# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:

    # создаём объект комплексного числа
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # создаём метод для отображения комплексного числа
    def __str__(self):
        return f'({self.x}, {self.y}i)'

    # создаём метод сложения комплексных чисел
    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    # создаём метод перемножения комплексных чисел
    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)


c1 = Complex(1, 2)
c2 = Complex(10, 20)

print(c1)
print(c1 + c2)
print(c1 * c2)
