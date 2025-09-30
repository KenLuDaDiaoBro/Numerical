import math

# 定義函數 f(t)
def f(t):
    return -1 * t**(-7 / 4) * math.sin(1 / t)  # 修正 sin(t**-1) 為 1/t

# 設定積分範圍與分點數
a = 9    # 起點
b = 1  # 終點
n = 4  # 分段數
h = (b - a) / (2 * n)  # 步長，確保是正數

# 初始化結果
Ans = 0

# 套用 Composite Simpson’s Rule
for i in range(2 * n + 1):  
    if(i == 0) or (i == 2 * n):
        Ans += f(a + i * h)  # 當前 x 值
    elif i % 2 == 0:
        Ans += 2 * f(a + i * h)  # 奇數點加權 4
    else:
        Ans += 4 * f(a + i * h)  # 偶數點加權 2

Ans *= h / 3  # 套用辛普森公式
print(f"積分近似值: {Ans}")
