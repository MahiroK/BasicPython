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

def f(x):
    if (x) == 1:
     return(f"(a),(b)は互いに素である")
    else:
     return("f(a),(b)は互いに素でない")
    
print(f(x))


