
import time
num = 1
day=10
for i in range(day,1,-1):
    day-=1
    num1=(num+1)*2
    num=num1
    print("第",day,"天,猴子吃之前剩下",num,"个")
    time.sleep(1)
print("总共摘了",num,"个")
