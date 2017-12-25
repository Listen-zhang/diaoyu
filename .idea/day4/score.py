score =[]
#for  i in range(1,len(score)+1):
score.append(68)
score.append(87)
score.append(92)
score.append(100)
score.append(76)
score.append(88)
score.append(54)
score.append(89)
score.append(76)
score.append(61)
print(score[2])
print(score[0:5])
score.insert(2,59)
print(score)
num  = 76
print(score.count(num))

if num  in score :
    print("有")
else :
    print("没有")
print(score.index(100))

for a  in score :
     if a==59:
         n =  score.index(a)
         score[n]+=1;
print(score);
del score[0]
len(score)
score.sort()
print(score)
print("最低",score[0])
print("最高",score[len(score)-1])
score.reverse()
print(score)
print(score.pop())
score.append(88)
score.remove(88)
print(score)
score1=[80,61]
score2=[71,95,82]
print(score1+score2)
score2=[]
score2+=score1.copy()*5
print(score2)

