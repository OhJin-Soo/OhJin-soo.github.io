class Rectangle:
    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    def getArea(self):
        result1 = (self.a3 - self.a1) * (self.a4 - self.a2)
        return result1

    def getPerimeter(self):
        result2 = 2 * ((self.a3 - self.a1) + (self.a4 - self.a2))
        return result2

    def show(self):
        print (f"좌측 상단 꼭지점이 ({self.a1},{self.a2})이고 우측 하단 꼭지점이 ({self.a3},{self.a4})인 사각형입니다.")


r1 = Rectangle(5, 5, 20, 10)


a = r1.getArea()
p = r1.getPerimeter()


r1.show()
print(f'넓이는 {a}, 둘레는 {p}')
