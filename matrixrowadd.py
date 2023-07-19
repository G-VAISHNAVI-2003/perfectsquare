r = int(input())
c = int(input())
arr = [[int(input())
       for i in range(c)]
       for j in range(r)]
print(arr)
row = 0
cl = []
for i in range(r):
    for j in range(c):
        row = row + arr[i][j]
    cl.append(row)
    row = 0
print(cl)
