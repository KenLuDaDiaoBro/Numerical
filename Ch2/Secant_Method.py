X0 = 0
X1 = 1
Error = 0.1

def F(x):
    return x ** 5 - 8 * x ** 4 + 44 * x ** 3 - 91 * x ** 2 + 85 * x - 26

counter = 2
while(True):
    dF_X0 = (F(X1) - F(X0)) / (X1 - X0)
    X2 = round(((X0 - F(X0) / dF_X0)) , 3)
    print(f"X{counter}: {X2}")
    if(abs(X2 - X1) < Error):
        print(f"ANS: {X2}")
        break
    X0 = X1
    X1 = X2
    counter += 1       
        