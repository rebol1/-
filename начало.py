class Rectangl:

    def __init__(self, width, length, rectang1=1):
        self.width = width
        self.length = length
        self.rectang1 = rectang1

    def square(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2

    def __str__(self):
        return f"Прямоугольник № {self.rectang1} с шириной {self.width} и длиной {self.length}"


a = Rectangl(4, 3,1)
print(a.length, a.width)
print(a.square())
print(a.perimeter())
print(a)
