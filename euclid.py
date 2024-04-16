def gcd (a,b):
    r = a % b
    while r != 0:
     a,b = b,r
     r = a % b 
    return b

if  __name__ == '__main__':
    a = int(input("aの値を入力:"))
    b = int(input("bの値を入力:"))

    GCD = gcd(a,b)

    print (f"({a},{b})→gcd: {GCD}")