l = list(map(int, input().split()))

print("bust" if sum(l) >= 22 else "win")