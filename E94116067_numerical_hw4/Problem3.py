import math

def f(x, y):
    return 2 * y * math.sin(x) + math.cos(x)**2

Exact = 0.51185
a = 0
b = math.pi / 4
n = 4
m = 4
h = (b - a) / (2 * n)

Ans = 0
for i in range(2 * n + 1):
    x = a + i * h
    g1 = math.sin(x)
    g2 = math.cos(x)
    k = (g2 - g1) / (2 * m)

    inner = 0
    for j in range(2 * m + 1):
        y = g1 + j * k
        
        if j == 0 or j == 2 * m:
            wy = 1
        elif j % 2 == 1:
            wy = 4
        else:
            wy = 2
        inner += wy * f(x, y)

    inner *= k / 3

    if i == 0 or i == 2 * n:
        wx = 1
    elif i % 2 == 1:
        wx = 4
    else:
        wx = 2

    Ans += wx * inner

Ans *= h / 3
Ea = abs(Exact - Ans)
print(f"a: {Ans:.5f}")

x = [-0.775, 0.0, 0.775]
c = [0.556, 0.889, 0.556]

Ans = 0
for i in range(3):
    Newx = (b + a) / 2 + x[i] * (b - a) / 2
    sinx = math.sin(Newx)
    cosx = math.cos(Newx)
    G1 = (cosx - sinx) / 2
    G2 = (cosx + sinx) / 2

    for j in range(3):
        Newy = G1 * x[j] + G2
        Ans += c[i] * c[j] * G1 * f(Newx, Newy)

Ans *= (b - a) / 2
print(f"b: {Ans:.5f}")
Eb = abs(Exact - Ans)
print(f"c: Simpson: {Ea:.5f} , Gauss: {Eb:.5f}")
