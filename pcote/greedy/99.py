# def until_one(n, k, cnt):
#     if n == 1:
#         print(cnt)
#         return
#     if n % k == 0:
#         until_one(n / k, k, cnt+1)
#     else:
#         until_one(n - 1, k, cnt+1)
#
# until_one(*map(int, input().split()), cnt=0)


n, k = map(int, input().split())
cnt = 0

while True:
    if n == 1:
        print(cnt)
        break
    if n % k == 0:
        n = n / k
    else:
        n -= 1
    cnt += 1