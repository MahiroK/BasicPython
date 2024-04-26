a,b = input("a: "),input("b: ")
a,b = int(a),int(b)

#　4-8行目を削除しました。

def gcd (a,b):
    if b > a:
        a,b = b,a 
    while b:
        a,b = b,a%b
    return a
x = gcd(a,b)

#(3)の最大公約数を書いていなかったので、追加しています。
print (x)

#ここから(4)の互いに素の判定を関数化しました。
#4/25 関数名を変更してみました。
#4/25 bool型に変更しました。

def judge(a,b):
    x = gcd(a,b)
    if  x == 1:
     return True
    else:
     return False

a,b = input("a: "),input("b: ")
a,b = int(a),int(b)

print(judge(a,b))

