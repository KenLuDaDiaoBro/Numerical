P0 = 0
P1 = 1
Error = 0.1

def F(x):
    return x ** 5 - 8 * x ** 4 + 44 * x ** 3 - 91 * x ** 2 + 85 * x - 26

counter = 1
while(True):
    F_P0 = F(P0) #負
    F_P1 = F(P1) #正
    P2 = P0 - ((P1 - P0) * F_P0 / (F_P1 - F_P0))
    F_P2 = round(F(P2) , 3)
    print(f"{counter}: {F_P2}")
    if(abs(F_P2) < Error):
        print(f"ANS: {P2:.8f}")
        break
    elif(F_P2 < 0):
        P0 = P2
    else:
        P1 = P2
    counter += 1
    