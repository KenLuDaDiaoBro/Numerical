import math
import sys

try:
    import pandas as pd
except ImportError:
    print("請先安裝 pandas")
    sys.exit(1)

pd.set_option('display.float_format' , '{:.4f}'.format)

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("請先安裝 matplotlib")
    sys.exit(1)

def f(x):
    return x**2 * math.sin(x)

c = 0
d = 1
m = 16
S = 4
step = (d - c) / (2 * m - 1)
x = [(c + i * step) for i in range(2 * m)]
z = [math.pi * (2 * (x - c) / (d - c) - 1) for x in x]

a = [0.0] * (S + 1)
b = [0.0] * (S + 1)

for i in range(S + 1):
    k = i
    for j in range(2 * m):
        a[k] += f(x[j]) * math.cos(k * z[j]) / m
        b[k] += f(x[j]) * math.sin(k * z[j]) / m
        
def S4(z):
    return 0.5 * a[0] + sum(a[k] * math.cos(k * z) + b[k] * math.sin(k * z) for k in range(1 , S + 1))
    
print(f"(a)\na0 = {a[0]:.4f}")
for i in range(S):
    num = i + 1
    print(f"a{num} = {a[num]:.4f} , b{num} = {b[num]:.4f}")
    
Ans = sum(S4(z[i]) / (2 * m - 1) for i in range(2 * m - 1))
print(f"(b)\nAns: {Ans:.4f}")

Real_y = [f(x) for x in x]
Approx_y = [S4(z) for z in z]
Errors = [abs(Ry - Ay) for Ry , Ay in zip(x , z)]
    
Real = math.cos(1) + 2 * math.sin(1) - 2
Ab = abs(Real - Ans)
Re = Ab / abs(Real) * 100

df_points = pd.DataFrame({
    'x':          z,
    'f(x)':       Real_y,
    'S4(x)':      Approx_y,
    'point_err':  Errors
})

print("(c)")
print(df_points.to_string(index=False))

print(f"\nf(x) Integral: {Real:.4f} , S4(Z) Integral: {Ans:.4f}")
print(f"\nAbsolute Error: {Ab:.4f} , Relative Error: {Re:.4f}%")

E = sum((f(x[i]) - S4(z[i]))**2 for i in range(2 * m))
print(f"(d)\nSquare Error: {E:.4f}")

x_plot = [c + i * (d - c) / (2 * m - 1) for i in range(2 * m)]
z_plot = [math.pi * (2 * (xi - c) / (d - c) - 1) for xi in x_plot]
y_f    = [xi**2 * math.sin(xi)  for xi in x_plot]
y_S4   = [S4(zi)                for zi in z_plot]

plt.plot(x_plot, y_f,  label='Exact (f(x))')
plt.plot(x_plot, y_S4, '--', label='Approx (S4)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x) vs. S4 on [0,1]')
plt.legend()
plt.grid(True)
plt.show()