import math

# Define the function f(x, y)
def f(x, y):
    return 2 * y * math.sin(x) + math.cos(x)**2

# Parameters
a = 0
b = math.pi / 4
n = 4  # x-direction subdivisions (must be even)
m = 4  # y-direction subdivisions (must be even)
hx = (b - a) / (2 * n)  # as per the note: h = (b-a)/2n

# Composite 2D Simpson's rule based on the definition from the image
total = 0
for i in range(2 * n + 1):
    x = a + i * hx
    g1 = math.sin(x)
    g2 = math.cos(x)
    k = (g2 - g1) / (2 * m)

    inner = 0
    for j in range(2 * m + 1):
        y = g1 + j * k
        # y direction weights
        if j == 0 or j == 2 * m:
            wy = 1
        elif j % 2 == 1:
            wy = 4
        else:
            wy = 2
        inner += wy * f(x, y)

    inner *= k / 3

    # x direction weights
    if i == 0 or i == 2 * n:
        wx = 1
    elif i % 2 == 1:
        wx = 4
    else:
        wx = 2

    total += wx * inner

total *= hx / 3
print(total)
