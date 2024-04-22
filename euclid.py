a,b = input("a: "),input("b: ")
a,b = int(a),int(b)

def gcd (a,b):
    if b == 0:
        return a
    else:
        return gcd (b,a%b)

x = gcd(a,b)
def gcd (a,b):
    if b > a:
        a,b = b,a 
    while b:
        a,b = b,a%b
        return a


if (x) <= 1:
    print(f"(a),(b)は互いに素である")
else:
    print("f(a),(b)は互いに素でない")