# _, m, k = map(int, input().split())
# target = sorted(list(map(int, input().split())), reverse=True)
# cnt = 0
#
# first = target[0]
# second = target[1]
#
#
# while m > 0:
#     for i in range(k):
#         cnt += first
#         m -= 1
#     cnt += second
#     m -= 1
#
# print(cnt)

_, m, k = map(int, input().split())

target = sorted(list(map(int, input().split())), reverse=True)

print(((m // (k + 1)) * (target[0] * k + target[1])) + (m % (k + 1) * target[0]))