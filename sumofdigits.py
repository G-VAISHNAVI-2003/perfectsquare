def sumofdigits():
    n = int(input())
    target = int(input()) #input of digit to check from N
    count = 0
    while(n>0):
        rem = n%10
        if(rem == target):
            count += 1
        n = n//10
    print(count)
sumofdigits()