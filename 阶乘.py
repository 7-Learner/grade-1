M=eval(input("请输入您想要阶乘的数字："))
S=1
i=1
while i<=M:
    S=i*S
    i=i+1
print(M,"的阶乘为",S)