r = int(input())
c = int(input())
arr = [[int(input())
       for i in range(c)]
       for j in range(r)]
print(arr)
for i in range(r):
    for j in range(i+1,c):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)