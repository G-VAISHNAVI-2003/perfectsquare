def pairSum():
    s = int(input())
    arr= list(map(int,input().split()))

    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == s:
                print(arr[i], arr[j])

    return -1
pairSum()
