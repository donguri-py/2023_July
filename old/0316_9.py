l = list(map(int, input().split()))

if l[0] >= l[-1]:
    print(1)
elif l[0] + 1 <= l[-1] <= l[1]:
    print(l[2] / (l[1] - l[0]))
else:
    print(0)