import math

def F(x):
    lnx = math.log(x)
    return x ** 2 * lnx

Exact = 0.19226
a = 1
b = 1.5
c = [0.556 , 0.889 , 0.556]
x = [-0.775 , 0 , 0.775]
Ans = 0
for i in range(3):
    Cr = (a + b + (b - a) * x[i]) / 2
    Ans += c[i] * F(Cr)

Ans *= (b - a) / 2
Error = abs(Exact - Ans)
print(f"n = 3: {Ans:.5f} , Error: {Error:.5f}")

c = [0.348 , 0.652 , 0.652 , 0.348]
x = [-0.861 , 0.340 , -0.340 , 0.861]
Ans = 0
for i in range(4):
    Cr = (a + b + (b - a) * x[i]) / 2
    Ans += c[i] * F(Cr)

Ans *= (b - a) / 2
Error = abs(Exact - Ans)
print(f"n = 4: {Ans:.5f} , Error: {Error:.5f}")
