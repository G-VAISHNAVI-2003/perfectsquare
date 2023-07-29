def replaceright():
    arr = list(map(int, input().split()))
    li = []
    for i in range(len(arr)):
        s = -1
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                s = arr[j]
                break
        li.append(s)
    print(*li)
replaceright()
