import math
import numpy as np
import matplotlib.pyplot as plt

x_min = 0
x_max = 1
t_min = 0
h = 0.1
k = 0.1
n = int((x_max - x_min) / h - 1)
alpha = 1.0
lambda_sq = alpha**2 * (k / h)**2
t_steps = 11

x = [x_min + i * h for i in range(n + 2)]
t = [t_min + i * k for i in range(t_steps)]
A = [[0.0 for _ in range(n)] for _ in range(n)]  # n x n
for i in range(n):
    A[i][i] = 2 * (1 - lambda_sq)
    if i > 0:
        A[i][i - 1] = lambda_sq
    if i < n - 1:
        A[i][i + 1] = lambda_sq
p = [[0.0 for _ in range(t_steps)] for _ in range(n + 2)]

for i in range(n + 2):
    p[i][0] = math.cos(2 * math.pi * x[i])
for i in range(n + 2):
    p[i][1] = (1 - 0.02 * math.pi**2) * math.cos(2 * math.pi * x[i]) + 0.2 * math.pi * math.sin(2 * math.pi * x[i])
for j in range(t_steps):
    p[0][j] = 1.0
    p[n + 1][j] = 2.0

for j in range(1, t_steps - 1): # 1 ~ 9
    p_j = [p[i][j] for i in range(1, n + 1)]  # P_j
    p_j_minus_1 = [p[i][j - 1] for i in range(1, n + 1)]  # P_j-1
    p_j_plus_1 = [0.0 for _ in range(n)]  # P_j+1
    
    for i in range(n):
        for k in range(n):
            p_j_plus_1[i] += A[i][k] * p_j[k]
        p_j_plus_1[i] -= p_j_minus_1[i]
        
    p_j_plus_1[0] += 1.0  # p_{0,j} = 1
    p_j_plus_1[n-1] += 2.0  # p_{n+1,j} = 2
        
    for i in range(n):
        p[i + 1][j + 1] = p_j_plus_1[i]

print("x\t t\t p(x,t)")
for j in range(t_steps):
    for i in range(n + 2):
        print(f"{x[i]:.3f}\t{t[j]:.3f}\t{p[i][j]:.6f}")

X, T = np.meshgrid(x, t)
P = np.array(p).T

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, T, P, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('p(x,t)')
ax.set_title('Problem 4')
fig.colorbar(surf, label='p(x,t)')
plt.tight_layout()
plt.show()