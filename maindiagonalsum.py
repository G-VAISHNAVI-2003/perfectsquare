r = int(input())
c = int(input())
mat = [[int(input())
       for i in range(c)]
       for j in range(r)]
dia = 0
dl = []
for i in range(min(r,c)):
    dia = dia+mat[i][i]
dl.append(dia)
print(dl)
        
        