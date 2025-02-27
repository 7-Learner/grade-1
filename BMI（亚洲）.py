height=eval(input("请输入您的身高（米）:"))
weight=eval(input("请输入您的体重（kg):"))
BMI=weight/(height**2)
print("BMI=",BMI)
print("根据亚洲人的BMI参考标准，您的的身体",end="")
if BMI<18.5:
    print("偏瘦")
elif 18.5<=BMI<23:
    print("正常")
elif BMI in range(23,25):
    print("偏胖")
elif BMI in range(25,30):
    print("肥胖")
elif BMI>=30:
    print("重度肥胖")
import time
time.sleep(6)
