# num=int(input("请输入"));
# bio = []
# for ii in range(1,num+1):
#     bio.append(ii)
# i = 0
# print(bio)
# while True:
#     if len(bio)==1:
#         break
#     i=i+1;
#     if i%3==0:
#      bio.pop(0)
#     else:
#      bio.append(bio.pop(0))
# print(bio)
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
    print("{0} c出现了 {1}次".format(key,i.get(key)))