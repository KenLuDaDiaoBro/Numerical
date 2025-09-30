import math

def F(x):
    Ex = math.exp(x)
    Sinx = math.sin(4 * x)
    return Ex * Sinx

a = 1
b = 2
h = 0.01
n = (b - a) / (2 * h)
Ans = F(a)    
for i in range(1 , int(2 * n)):
    Ans += 2 * F(a + i * h)

Ans += F(b)
Ans *= h / 2
print(f"Ans: {Ans}")
