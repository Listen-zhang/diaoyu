#1.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
aa = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

bb = [[5,8,1],
    [6,7,3],
    [4,5,9]]
d = []
for a in range(min(len(aa),len(bb))):
    c = [aa[a][i] + bb[a][i] for i in range(min(len(aa[a]), len(bb[a])))]
    d.append(c)
print(d)