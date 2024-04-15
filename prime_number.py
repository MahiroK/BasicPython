# 自然数nが与えられたとき、素数であるか素数でないかを判定する問題
#(1) 61が素数であること
#(2) 10が素数でないこと


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True 

n = int(input("数値を入力してください: "))
if is_prime(n):
    print("素数と判定されました.")
else:
    print("素数ではありません.")

