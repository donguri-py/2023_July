n = int(input())

l = list(map(int, input().split()))

min_l = l[0]
for i in range(n):
    if l[i] < min_l:
        min_l = l[i]
print(min_l)