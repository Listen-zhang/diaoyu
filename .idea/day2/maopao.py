'''
冒泡
'''
array = [1,2,3,6,5,4]
for i in range(len(array)):
    for j in range(len(array)-1):
        if array[j] > array[j + 1]:
            muo =  array[j + 1]
            array[j+1]  = array[j]
            array[j] = muo
print(array)
print(str(123)+'123')
["123"]["456"]
["1*4 ""1*5"]

str = "adc我爱中国";
ai = str[4] #下标为4的
print(ai)
sub  = str[4:] # 下标为4以后的
sub = str[4:6] #4到6左闭右开
