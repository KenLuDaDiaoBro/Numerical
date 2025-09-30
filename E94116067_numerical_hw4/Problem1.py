import math

def F(x):
    Ex = math.exp(x)
    Sinx = math.sin(4 * x)
    return Ex * Sinx

a = 1
b = 2
h = 0.1
n = (b - a) / (2 * h)

Ans = F(a)    
for i in range(1 , int(2 * n)):
    Ans += 2 * F(a + i * h)

Ans += F(b)
Ans *= h / 2
print(f"a: {Ans:.3f}")

Ans = F(1)   
Ans += 4 * F(a + h)
for i in range(2 , int(n) + 1):
    Ans += 2 * F(a + (2 * i - 2) * h)
    Ans += 4 * F(a + (2 * i - 1) * h)

Ans += F(2)
Ans *= h / 3

print(f"b: {Ans:.3f}")

Ans = 0
for i in range(1 , int(n) + 1):
    Ans += F(a + (2 * i - 1) * h)

Ans *= 2 * h

print(f"c: {Ans:.3f}")
