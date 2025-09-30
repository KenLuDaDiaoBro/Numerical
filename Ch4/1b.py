import math

def F(x):
    Ex = math.exp(x)
    Sinx = math.sin(4 * x)
    return Ex * Sinx

a = 1
b = 2
h = 0.1
n = (b - a) / (2 * h)
Ans = F(1)   
Ans += 4 * F(a + h)
for i in range(2 , int(n) + 1):
    Ans += 2 * F(a + (2 * i - 2) * h)
    Ans += 4 * F(a + (2 * i - 1) * h)

Ans += F(2)
Ans *= h / 3

print(f"Ans: {Ans}")
