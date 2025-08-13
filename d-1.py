class Circle:
    # コンストラクタ（初期化メソッド）
    def ___init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
