X = [0.3 , 0.4 , 0.5 , 0.6]
E_X = [0.740818 , 0.670320 , 0.606531 , 0.548812]
Error = 0.00001
Guess = 0.6

while(True):
    ANS = 0
    for i in range(0 , 4):
        L = 1
        for j in range(0 , 4):
            if(i != j):
                L = L * (Guess - X[j]) / (X[i] - X[j])
        ANS = ANS + E_X[i] * L 
    if abs(ANS - Guess) < Error:
        break
    else:
        Guess = ANS
print(f"x: {ANS:.8f}")
