from math import sin,pi
# --example--
a = int('0')
b = pi/int('2')
n = int('100')

# 短冊の幅Δx
h = (b-a)/n


# 面積の総和
s = 0
# 4/16 変更：　range内を（1,n+1）に変更しました
# 問題文の式をもとに修正してみました。

for i in range(1,n+1):
    x1 = a+h*(i-1)
    x2 = a+h*i
    f1 = sin(x1)    # 上底
    f2 = sin(x2)    # 下底
    # 面積
    s += h * (f1+f2)/2

# 結果の表示(小数点以下10桁)
print("{:.10f}".format(s))

# print(sin(0))
# >>> 0
# -----------
