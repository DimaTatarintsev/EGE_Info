def digits_even(x):
    s = str(x)
    for ch in s:
        if ch in '13579':
            return False
    return True

def find_numbers(limit_count=5, start_n=1_000_000):
    found = []
    m = 1
    A_list = []
    while True:
        A = 111 * m
        if digits_even(A):
            A_list.append(A)
        m += 1
        if A > 10_000_000: 
            break
    powers = []
    k = 1
    while True:
        p = 5 ** k
        powers.append(p)
        k += 1
        if p > 10_000_000:
            break
    
    candidates = []
    for A in A_list:
        for k, p in enumerate(powers, start=1):
            n = A + p
            if n > start_n:
                candidates.append((n, k))
    candidates.sort(key=lambda x: x[0])
    seen = set()
    for n, k in candidates:
        if n not in seen:
            seen.add(n)
            found.append((n, k))
            if len(found) >= limit_count:
                break
    return found

result = find_numbers(5, 1_000_000)
for n, k in result:
    print(n, k)
