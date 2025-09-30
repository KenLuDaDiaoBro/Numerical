import math
import sys

try:
    import pandas as pd
except ImportError:
    print("請先安裝 pandas")
    sys.exit(1)

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("請先安裝 matplotlib")
    sys.exit(1)

def Y(t , h , n):
    ti = [t + i * h for i in range(n + 1)]
    yi = [round(t * math.tan(math.log(t)) , 8) for t in ti]
    return ti , yi

def F(t , y):
    return 1 + (y / t) + (y / t)**2

def Ft(t , y):
    return -y / t**2 - 2 * y**2 / t**3

def Fy(t , y):
    return 1 / t + 2 * y / t**2

def EulerMethod (t , y , h , n):
    ti = [t + i * h for i in range(n + 1)]
    yi = [0] * (n + 1)
    yi[0] = y
    for i in range(n):
        yi[i + 1] = round(yi[i] + F(ti[i] , yi[i]) * h , 8)
    return yi

def TaylorMethod (t , y , h , n):
    ti = [t + i * h for i in range(n + 1)]
    yi = [0] * (n + 1)
    yi[0] = y
    for i in range(n):
        Fi = F(ti[i] , yi[i])
        FT = Ft(ti[i] , yi[i])
        FY = Fy(ti[i] , yi[i])
        yi[i + 1] = round(yi[i] + h * (Fi + h / 2 * (FT + Fi * FY)) , 8)
    return yi
        
t = 1
y = 0
h = 0.1
t_end = 2
n = int((t_end - t) / h)
ti , yi = Y(t , h , n)
yEi = EulerMethod (t , y , h , n)
yTi = TaylorMethod (t , y , h , n)

err_euler  = [round(abs(ex - eu), 8) for ex , eu in zip(yi, yEi)]
err_taylor = [round(abs(ex - tr), 8) for ex , tr in zip(yi, yTi)]

print("1.a")
df_euler = pd.DataFrame({
    't':        ti,
    'y_exact':  yi,
    'y_euler':  yEi,
    'error':    err_euler
})
print("Euler Method Results:")
print(df_euler.to_string(index=False))

plt.plot(ti , yi , '-' , label='Exact Solution')
plt.plot(ti , yEi , '--' , label='Euler Approximation')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Exact vs Euler')
plt.legend()
plt.grid(True)
plt.show()

print("1.b")
df_taylor = pd.DataFrame({
    't':         ti,
    'y_exact':   yi,
    'y_Taylor2': yTi,
    'error':     err_taylor
})
print("\nTaylor Method (Order 2) Results:")
print(df_taylor.to_string(index=False))

plt.plot(ti, yi , '-', label='Exact Solution')
plt.plot(ti, yTi , '--', label='Taylor Order 2')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Exact vs Taylor')
plt.legend()
plt.grid(True)
plt.show()