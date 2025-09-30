import math

P_X = [0.698 , 0.733 , 0.768 , 0.803 , 0.838]
P_Y = [0.7661 , 0.7432 , 0.7193 , 0.6946 , 0.6690]
P_ACCX = 0.750
P_ACCY = 0.7317

for order in range(1 , 5):
    F = 0
    for i in range(order + 1):
        L = 1
        for j in range(order + 1):  
            if(i != j):
                L = L * (P_ACCX - P_X[j]) / (P_X[i] - P_X[j])
        F = F + P_Y[i] * L
    F = round(F , 8)
    
    EB = 1 / math.factorial(order)
    c = (P_X[order] - P_X[0]) / 99999
    max = 0
    cos = 0
    Now_Step = P_X[0]
    for step in range(100000):
        Tem = EB
        for i in range(order + 1):
            Tem *= (Now_Step - P_X[i])
        #print(Tem)
        if(abs(Tem) > max):
            max = abs(Tem)
        Now_Step += c
    print(f"Order {order}: {F:.8f} , Error Bound: {max}")
