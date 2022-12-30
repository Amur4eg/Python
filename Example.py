a, b = input(), input()
if a != b and bool(a):
    k = 0
    for i in range(len(a)):
        if a[i] in b[k:] :
            k = b.find(a[i])
        else:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')
