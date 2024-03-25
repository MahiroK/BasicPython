a = 1
b = -6
c = 9

# 1問目(1)

import math

# 2次方程式の解を計算する関数
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (real_part, imaginary_part), (real_part, -imaginary_part)

# 係数を入力
a = float(input("1: "))
b = float(input("-6: "))
c = float(input("9: "))

# 解を計算
roots = solve_quadratic(a, b, c)

# 結果を表示
print("解は: ", roots)


# (2)
a = 1
b = -6
c = 9

import math
# 2次方程式の解を計算する関数
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (real_part, imaginary_part), (real_part, -imaginary_part)

# 係数を入力
a = float(input("1: "))
b = float(input("-6: "))
c = float(input("9: "))

# 解を計算
roots = solve_quadratic(a, b, c)

# 結果を表示
print("解は: ", roots)
