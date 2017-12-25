num = input("请输入内容")
i = {}
for  o in num :
  n = i.get(o);
  if n is None :
    i.__setitem__(o,1)
  else:
    i.__setitem__(o,n+1);
print(i)
for key in i:
    print("{0} 出现了 {1}次".format(key,i.get(key)))
di  = sorted(i.items(),key=lambda d:-d[1])
print("-----------------------------")
print(di)
for c in di :
    print("{0} 出现了 {1}次".format(c[0],c[1]))
print("-----------------------------")
di  = sorted(i.items(),key=lambda d:(-d[1],d[0].encode("gbk")))
for i in di :
    print("{0} 出现了 {1}次".format(i[0],i[1]))
