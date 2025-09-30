X0 = 1
Error = 0.1

def F(x):
    return x ** 5 - 8 * x ** 4 + 44 * x ** 3 - 91 * x ** 2 + 85 * x - 26

def dF(x):
    return 5 * x ** 4 - 32 * x ** 3 + 132 * x ** 2 - 182 * x + 85

counter = 1
while(True):
    X1 = round((X0 - F(X0) / dF(X0)) , 3)
    print(f"X{counter}: {X1}")
    if(abs(X1 - X0) < Error):
        print(f"ANS: {X1}")
        break
    X0 = X1
    counter += 1    
        