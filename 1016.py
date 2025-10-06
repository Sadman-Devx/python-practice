a, b = map(int, input().split())
b = abs(b)
q = a // b
r = a % b

#if r < 0:
    #r += b
    #q -= 1

print(f"{q} {r}")