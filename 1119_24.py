l = list(map(int, input().split()))
l2 = []
for i in l:
    if i <= 2:
        l2.append(i)
print(len(l2))