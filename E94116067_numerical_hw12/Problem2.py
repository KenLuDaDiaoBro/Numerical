import numpy as np
import matplotlib.pyplot as plt

r_min = 0.5
r_max = 1.0
t_min = 0.0
t_max = 10.0
h = 0.1
k = 0.5
K = 0.1
n = int((r_max - r_min) / h - 1)
t_steps = int(t_max / k) + 1
lambda_val = 4 * K * k / (h ** 2)

r = [r_min + i * h for i in range(n + 2)]  # [0.5, 0.6, ..., 1.0]
t = [t_min + j * k for j in range(t_steps)]  # [0, 0.5, ..., 10.0]

def gauss_elimination(A, F):
    size = len(F)
    for i in range(size):
        max_element = abs(A[i][i])
        max_row = i
        for k in range(i + 1, size):
            if abs(A[k][i]) > max_element:
                max_element = abs(A[k][i])
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        F[i], F[max_row] = F[max_row], F[i]
        for k in range(i + 1, size):
            if A[i][i] == 0:
                raise ValueError("No Solution")
            factor = A[k][i] / A[i][i]
            for j in range(i, size):
                A[k][j] -= factor * A[i][j]
            F[k] -= factor * F[i]
    
    U = [0] * size
    for i in range(size - 1, -1, -1):
        if A[i][i] == 0:
            raise ValueError("No Solution")
        U[i] = F[i]
        for j in range(i + 1, size):
            U[i] -= A[i][j] * U[j]
        U[i] /= A[i][i]
    return U

def matrix_vector_multiply(A, v):
    n = len(v)
    result = [0.0] * n
    for i in range(n):
        for j in range(n):
            result[i] += A[i][j] * v[j]
    return result

def initialize_T():
    T = [[0.0] * t_steps for _ in range(n + 2)]
    for i in range(n + 2):
        T[i][0] = 200 * (r[i] - 0.5)
    for j in range(t_steps):
        T[n + 1][j] = 100 + 40 * t[j]
    return T

def forward_difference():
    T = initialize_T()
    for j in range(t_steps - 1):
        A = [[0.0] * n for _ in range(n)] # A[t][r]
        for i in range(1, n + 1):
            idx = i - 1
            if i > 1:
                A[idx][idx-1] = lambda_val * (1 - h / (2 * r[i]))
            A[idx][idx] = -2 * lambda_val + 1
            if i < n:
                A[idx][idx+1] = lambda_val * (1 + h / (2 * r[i]))
        T_j = [T[i][j] for i in range(1, n + 1)]
        T_j_next = matrix_vector_multiply(A, T_j)
        for i in range(1, n + 1):
            T[i][j + 1] = T_j_next[i - 1]
        T[0][j + 1] = T[1][j + 1] / 1.3
    return T

def backward_difference():
    T = initialize_T()
    for j in range(t_steps - 1):
        A = [[0.0] * n for _ in range(n)]
        F = [0.0] * n
        for i in range(1, n + 1):
            idx = i - 1
            if i > 1:
                A[idx][idx-1] = -lambda_val * (1 - h / (2 * r[i]))
            A[idx][idx] = 1 + 2 * lambda_val
            if i < n:
                A[idx][idx+1] = -lambda_val * (1 + h / (2 * r[i]))
            F[idx] = T[i][j]
        A[0][0] += lambda_val * (1 - 0.05 / r[1]) / 1.3
        F[n-1] += lambda_val * (1 + 0.05 / r[n]) * T[n + 1][j + 1]
        T_j_next = gauss_elimination(A, F)
        for i in range(1, n + 1):
            T[i][j + 1] = T_j_next[i - 1]
        T[0][j + 1] = T[1][j + 1] / 1.3
    return T

def crank_nicolson():
    T = initialize_T()
    for j in range(t_steps - 1):
        A = [[0.0] * n for _ in range(n)]
        B = [[0.0] * n for _ in range(n)]
        F = [0.0] * n
        for i in range(1, n + 1):
            idx = i - 1
            coeff_minus = lambda_val / 2 * (1 - 0.05 / r[i])
            coeff_plus = lambda_val / 2 * (1 + 0.05 / r[i])
            if i > 1:
                A[idx][idx-1] = -coeff_minus
                B[idx][idx-1] = coeff_minus
            A[idx][idx] = 1 + lambda_val
            B[idx][idx] = 1 - lambda_val
            if i < n:
                A[idx][idx+1] = -coeff_plus
                B[idx][idx+1] = coeff_plus
        A[0][0] += (lambda_val / 2 * (1 - 0.05 / r[1])) / 1.3
        T_j = [T[i][j] for i in range(1, n + 1)]
        F = matrix_vector_multiply(B, T_j)
        F[n-1] += (lambda_val / 2 * (1 + 0.05 / r[n])) * (T[n + 1][j] + T[n + 1][j + 1])
        T_j_next = gauss_elimination(A, F)
        for i in range(1, n + 1):
            T[i][j + 1] = T_j_next[i - 1]
        T[0][j + 1] = T[1][j + 1] / 1.3
    return T

print("Forward-Difference Method")
T_forward = forward_difference()
print("r\t t\t T(r,t)")
for j in range(t_steps):
    for i in range(n + 2):
        print(f"{r[i]:.3f}\t{t[j]:.3f}\t{T_forward[i][j]:.6f}")
  
print("\nBackward-Difference Method")
T_backward = backward_difference()
print("r\t t\t T(r,t)")
for j in range(t_steps):
    for i in range(n + 2):
        print(f"{r[i]:.3f}\t{t[j]:.3f}\t{T_backward[i][j]:.6f}")

print("\nCrank-Nicolson Algorithm")
T_crank = crank_nicolson()
print("r\t t\t T(r,t)")
for j in range(t_steps):
    for i in range(n + 2):
        print(f"{r[i]:.3f}\t{t[j]:.3f}\t{T_crank[i][j]:.6f}")
        
R, T = np.meshgrid(r, t)
T_forward = np.array(T_forward).T  # Shape: (t_steps, n+2)
T_backward = np.array(T_backward).T
T_crank = np.array(T_crank).T

fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(111, projection='3d')
surf1 = ax1.plot_surface(T, R, T_forward, cmap='viridis')
ax1.set_xlabel('t')
ax1.set_ylabel('r')
ax1.set_zlabel('T(r,t)')
ax1.set_title('Forward-Difference Method')
fig1.colorbar(surf1, label='T(r,t)')
plt.tight_layout()

fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')
surf2 = ax2.plot_surface(T, R, T_backward, cmap='viridis')
ax2.set_xlabel('t')
ax2.set_ylabel('r')
ax2.set_zlabel('T(r,t)')
ax2.set_title('Backward-Difference Method')
fig2.colorbar(surf2, label='T(r,t)')
plt.tight_layout()

fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(111, projection='3d')
surf3 = ax3.plot_surface(T, R, T_crank, cmap='viridis')
ax3.set_xlabel('t')
ax3.set_ylabel('r')
ax3.set_zlabel('T(r,t)')
ax3.set_title('Crank-Nicolson Algorithm')
fig3.colorbar(surf3, label='T(r,t)')
plt.tight_layout()

plt.show()