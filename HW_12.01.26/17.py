with open('17.txt', 'r') as f:
    nums = list(map(int, f.read().split()))

mx2zn = max(x for x in nums if 10 <= x <= 99) if any(10 <= x <= 99 for x in nums) else -1
if mx2zn == -1:
    print(0, 0)
    exit()

cnt = 0
mx_sum = 0
for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i+1], nums[i+2]
    nat_cnt = (a > 0) + (b > 0) + (c > 0)
    if nat_cnt == 2 and (a + b + c) % mx2zn == 0:
        cnt += 1
        s = a + b + c
        if s > mx_sum:
            mx_sum = s

print(cnt, mx_sum)
