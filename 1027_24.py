x, y, z = map(int, input().split())
l = list(map(int, input().split()))
for i in l:
    if i == x:
        print(y)
    else:
        print(i)