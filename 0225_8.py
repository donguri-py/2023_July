n = int(input())
l = [1, 1]
for i in range(2, 35):
    l.append((l[i-1]) + (l[i-2]))
print(l)