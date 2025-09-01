coin = [500, 100, 50, 10]
last = int(input())
cnt = 0

for c in coin:
    cnt += last // c
    last = last % c

print(cnt)