# 自然数nが与えられたとき、素数であるか素数でないかを判定する問題
#(1) 61が素数であること
#(2) 10が素数でないこと

n = int(input("数値を入力してください: "))

def is_prime(n):

    #　if文・for文を用いて正誤判定をしました
    for i in range (2,n):
     if n % i == 0:
        return "素数ではありません"
    return "素数と判定されました"
    
     
result = is_prime(n)
print(result)    