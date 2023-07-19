r = int(input())
c = int(input())
arr = [[int(input())
       for i in range(c)]
       for j in range(r)]
print(arr)
row = 0
col = 0
cl = []
for i in range(c):
    for j in range(r):
        col = col + arr[j][i]
    cl.append(col)
    col = 0
print(cl)
