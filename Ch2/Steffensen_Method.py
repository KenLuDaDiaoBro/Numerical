P0_0 = 0.5
Error = 0.001

def F(x):
    return x ** 5 - 8 * x ** 4 + 44 * x ** 3 - 91 * x ** 2 + 85 * x - 26

P0_1 = F(P0_0)
P0_2 = F(P0_1)

counter = 1
while(True):
    P1_0 = round(P0_0 - (P0_1 - P0_0) ** 2 / (P0_2 - 2 * P0_1 + P0_0) , 3)
    print(f"P{counter}: {P1_0}")
    if(abs(P1_0 - P0_0) < Error):
        print(f"ANS: {P1_0}")
        break
    P0_0 = P1_0
    P0_1 = F(P1_0)
    P0_2 = F(P0_1)
    counter += 1   
    