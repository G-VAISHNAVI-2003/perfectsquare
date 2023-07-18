def perfect():
    n =  int(input())
    if n >=0 and int(n**0.5)**2 == n:
        return True
    else:
        return False
res = perfect()
print(res)
