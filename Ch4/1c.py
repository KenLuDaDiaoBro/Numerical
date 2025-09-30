import math

def F(x):
    Ex = math.exp(x)
    Sinx = math.sin(4 * x)
    return Ex * Sinx

a = 1
b = 2
h = 0.1
n = (b - a) / (2 * h)
Ans = 0
for i in range(1 , int(n) + 1):
    Ans += F(a + (2 * i - 1) * h)

Ans *= 2 * h

print(f"Ans: {Ans}")
