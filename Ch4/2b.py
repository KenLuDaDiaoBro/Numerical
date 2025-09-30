import math

def F(x):
    lnx = math.log(x)
    return x ** 2 * lnx

a = 1
b = 1.5
c = [0.348 , 0.652 , 0.652 , 0.348]
x = [-0.861 , 0.340 , -0.340 , 0.861]
Ans = 0
for i in range(4):
    Cr = (a + b + (b - a) * x[i]) / 2
    Ans += c[i] * F(Cr)

Ans *= (b - a) / 2
print(f"Ans: {Ans}")
