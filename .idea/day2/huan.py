r  = int(input('请输入人数：'))
r_1= 0;
list = []
while 1<=r:
    r-=1;
    r_1+=1;
    list.append(r_1)
c = 0;
d = 3
while len(list)!= 1:
    for  i in  list:
        c += 1;
        print(list)
        if c==d:
            d +=3
            list.remove(i)
print(list)