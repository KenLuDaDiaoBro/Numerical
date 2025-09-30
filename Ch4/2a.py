import math

def F(x):
    lnx = math.log(x)
    return x ** 2 * lnx

a = 1
b = 1.5
c = [0.556 , 0.889 , 0.556]
x = [-0.775 , 0 , 0.775]
Ans = 0
for i in range(3):
    Cr = (a + b + (b - a) * x[i]) / 2
    Ans += c[i] * F(Cr)

Ans *= (b - a) / 2
print(f"Ans: {Ans}")
