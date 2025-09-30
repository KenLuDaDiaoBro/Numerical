import math

def Fa(t):
    return -1 * t**(-7 / 4) * math.sin(1 / t)

def Fb(t):
    return -t**2 * math.sin(1 / t)


a = 9
b = 1
n = 4
h = (b - a) / (2 * n)

Ans = 0

for i in range(2 * n + 1):  
    if(i == 0) or (i == 2 * n):
        Ans += Fa(a + i * h)
    elif i % 2 == 0:
        Ans += 2 * Fa(a + i * h)
    else:
        Ans += 4 * Fa(a + i * h)

Ans *= h / 3
print(f"a: {Ans:.4f}")

a = 1
b = 0.0001
h = (b - a) / (2 * n)

Ans = 0

for i in range(2 * n + 1):  
    if(i == 0) or (i == 2 * n):
        Ans += Fb(a + i * h)
    elif i % 2 == 0:
        Ans += 2 * Fb(a + i * h)
    else:
        Ans += 4 * Fb(a + i * h)

Ans *= h / 3 
print(f"b: {Ans:.4f}")
