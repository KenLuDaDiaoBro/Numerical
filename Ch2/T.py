P0 = 0.5
P1 = -0.5
P2 = 0

def F(x):
    return 16 * x ** 4 - 40 * x ** 3 + 5 * x ** 2 + 20 * x + 6

while(True):
    Poly = [0] * 3
    Cr0 = F(P0) / ((P0 - P1) * (P0 - P2))
    Cr1 = F(P1) / ((P1 - P0) * (P1 - P2))
    Cr2 = F(P2) / ((P2 - P0) * (P2 - P1))
    Poly[0] = Cr0 + Cr1 + Cr2
    Poly[1] = 2 * (Cr0 * (P1 + P2) + Cr1 * (P0 + P2) + Cr2 * (P0 + P1))
    Poly[2] = Cr0 * P1 * P2 + Cr1 * P0 * P2 + Cr2 * P0 * P1
    