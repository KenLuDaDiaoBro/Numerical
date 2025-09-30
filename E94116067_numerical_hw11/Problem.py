import math
import matplotlib.pyplot as plt

def f_y1(x, z1, z2):
    return [z2, 2*z1 - (x+1)*z2 + (1-x*x)*math.exp(-x)]

def f_y2(x, z1, z2):
    return [z2, 2*z1 - (x+1)*z2]

def rk4_step(x, z, h, f):
    k1 = f(x, z[0], z[1])
    k2 = f(x + h/2, z[0] + h/2*k1[0], z[1] + h/2*k1[1])
    k3 = f(x + h/2, z[0] + h/2*k2[0], z[1] + h/2*k2[1])
    k4 = f(x + h, z[0] + h*k3[0], z[1] + h*k3[1])
    
    z_next = [
        z[0] + (h/6)*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]),
        z[1] + (h/6)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
    ]
    return z_next

def shooting_method(h):
    a, b = 0.0, 1.0
    n = int((b - a) / h)
    x_values = [a + i*h for i in range(n + 1)]

    y1_values = []
    z1 = [1.0, 0.0]
    y2_values = []
    z2 = [0.0, 1.0]
    for x in x_values:
        y1_values.append(z1[0])
        y2_values.append(z2[0])
        if x < b:  # Don't compute beyond x=1
            z1 = rk4_step(x, z1, h, f_y1)
            z2 = rk4_step(x, z2, h, f_y2)
    
    # Compute c = (y(1) - y1(1)) / y2(1)
    y1_b = y1_values[-1]  # y1(1)
    y2_b = y2_values[-1]  # y2(1)
    if abs(y2_b) < 1e-10:  # Check if y2(1) is zero
        print("Warning: y2(1) is zero, try different initial slope.")
        return None
    c = (2.0 - y1_b) / y2_b  # y(1) = 2

    # Compute final solution y(x) = y1(x) + c*y2(x)
    y_values = [y1 + c*y2 for y1, y2 in zip(y1_values, y2_values)]

    return x_values, y_values





def p(x):
    return -(x + 1)

def q(x):
    return 2

def r(x):
    return (1 - x*x) * math.exp(-x)

def tridiagonal_solver(a, b, c, d):
    n = len(d)
    c_prime = [0] * n
    d_prime = [0] * n
    x = [0] * n

    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]
    for i in range(1, n):
        denom = b[i] - a[i] * c_prime[i-1]
        c_prime[i] = c[i] / denom if i < n-1 else 0
        d_prime[i] = (d[i] - a[i] * d_prime[i-1]) / denom

    x[n-1] = d_prime[n-1]
    for i in range(n-2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i+1]

    return x

def finite_difference_method(h):
    a, b = 0.0, 1.0
    n = int((b - a) / h) - 1  # n = 9
    x_values = [i * h for i in range(n + 2)]
    y_0, y_n1 = 1.0, 2.0

    lower = [0] * n
    diag = [0] * n
    upper = [0] * n
    F = [0] * n

    for i in range(n):
        x_i = x_values[i + 1]  # x_1 to x_9
        p_i = p(x_i)
        q_i = q(x_i)
        r_i = r(x_i)
        
        diag[i] = 2 + h * h * q_i  # 2 + h^2 * q_i
        if i < n - 1:
            upper[i] = -(1 - (h/2) * p_i)  # -(1 - (h/2) * p_i)
        if i > 0:
            lower[i] = -(1 + (h/2) * p_i)  # -(1 + (h/2) * p_i)
        
        # RHS vector
        if i == 0:
            F[i] = -h * h * r_i + (1 + (h/2) * p_i) * y_0
        elif i == n - 1:
            F[i] = -h * h * r_i + (1 - (h/2) * p_i) * y_n1
        else:
            F[i] = -h * h * r_i
            
    y_interior = tridiagonal_solver(lower, diag, upper, F)

    y_values = [y_0] + y_interior + [y_n1]

    return x_values, y_values





def y1(x): return 1 + x

def phi(x, i):
    return math.sin(i * math.pi * x)

def phi_prime(x, i):
    return i * math.pi * math.cos(i * math.pi * x)

def trapezoidal_integrate(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

def variation_method(h):
    a, b = 0.0, 1.0
    n_points = int((b - a) / h) + 1
    x_values = [i * h for i in range(n_points)]
    N = 5

    A = [[0 for _ in range(N)] for _ in range(N)]
    B = [0 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            def integrand_A(x):
                phi_i, phi_j = phi(x, i+1), phi(x, j+1)
                phi_i_prime, phi_j_prime = phi_prime(x, i+1), phi_prime(x, j+1)
                P = -math.exp(x * x / 2 + x)
                Q = -2 * math.exp(x * x / 2 + x)
                return (P * phi_i_prime * phi_j_prime + Q * phi_i * phi_j)
            A[i][j] = trapezoidal_integrate(integrand_A, a, b, n_points - 1)

        def integrand_b(x):
            phi_i = phi(x, i+1)
            f = (1 - x*x) * math.exp(x * x / 2)
            return (f * phi_i)
        B[i] = trapezoidal_integrate(integrand_b, a, b, n_points - 1)

    c = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            factor = A[j][i] / A[i][i]
            for k in range(i, N):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]
    for i in range(N-1, -1, -1):
        c[i] = B[i]
        for j in range(i+1, N):
            c[i] -= A[i][j] * c[j]
        c[i] /= A[i][i]

    def y_total(x, c):
        return y1(x) + sum(c[i-1] * phi(x, i) for i in range(1, 4))
    y_values = [y_total(x, c) for x in x_values]

    return x_values, y_values

if __name__ == "__main__":
    x_shoot, y_shoot = shooting_method(h=0.1)
    print("\nShooting Method\n")
    print("x\ty(x)")
    print("-" * 16)
    for x, y in zip(x_shoot, y_shoot):
        print(f"{x:.1f}\t{y:.6f}")
    
    x_finite, y_finite = finite_difference_method(h=0.1)
    print("\nFinite Difference Method\n")
    print("x\ty(x)")
    print("-" * 16)
    for x, y in zip(x_finite, y_finite):
        print(f"{x:.1f}\t{y:.6f}")
        
    x_var, y_var = variation_method(h=0.1)
    print("\nVariation Method\n")
    print("x\ty(x)")
    print("-" * 16)
    for x, y in zip(x_var, y_var):
        print(f"{x:.1f}\t{y:.6f}")
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_shoot, y_shoot, 'o-', label='Shooting Method', color='orange')
    plt.plot(x_finite, y_finite, '--', label='Finite Difference Method', color='green')
    plt.plot(x_var, y_var, '^-', label='Variation Method', color='red')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('Comparison of Numerical Methods for ODE')
    plt.legend()
    plt.grid(True)
    plt.show()

