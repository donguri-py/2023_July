x, y = map(int, input().split())

count = 0
while x < y:
    count += 1
    x += 10

print(count)