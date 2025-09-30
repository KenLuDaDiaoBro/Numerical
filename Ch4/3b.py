import math

def f(x, y):
    return 2 * y * math.sin(x) + math.cos(x)**2

a = 0
b = math.pi / 4

# Gaussian nodes and weights (approximate values)
x = [-0.775, 0.0, 0.775]
c = [0.556, 0.889, 0.556]

Ans = 0
for i in range(3):
    # 外積分：x 範圍 [a, b] 的變數變換
    x_val = (b + a) / 2 + x[i] * (b - a) / 2
    sinx = math.sin(x_val)
    cosx = math.cos(x_val)
    G1 = (cosx - sinx) / 2
    G2 = (cosx + sinx) / 2

    for j in range(3):
        y_val = G1 * x[j] + G2
        Ans += c[i] * c[j] * G1 * f(x_val, y_val)

Ans *= (b - a) / 2
print("Gaussian Quadrature result:", Ans)
