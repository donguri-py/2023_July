a, b = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(a, b)
# print(n)
# print(l)

for i in range(n):
    if a == l[i][0]:
        if b > l[i][1]:
            print("Low")
        else:
            print("High")
    elif a < l[i][0]:
        print("Low")
    else:
        print("High")