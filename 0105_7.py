n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l2 = []
for i in range(n):
    if l[i][0] == 1:
        l2.append(l[i][1])
    elif l[i][0] == 2:
        l2.pop(0)
    print(*l2)