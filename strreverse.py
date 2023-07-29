def strreverse():
    string = str(input())
    word = string.strip().split()
    result = ' '.join(word[::-1])
    print(result)
strreverse()