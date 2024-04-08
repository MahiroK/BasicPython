from math import sin,pi
# --example--
a = int('0')
b = pi/int('2')
n = int('100')

# 短冊の幅Δx
dx = (b-a)/n

# 面積の総和
s = 0
for i in range(1,100):
    x1 = a + dx*i
    x2 = a + dx*(i+1)
    f1 = sin(x1)    # 上底
    f2 = sin(x2)    # 下底
    # 面積
    s += dx * (f1+f2)/2

# 結果の表示(小数点以下10桁)
print("{:.10f}".format(s))

# print(sin(0))
# >>> 0
# -----------
