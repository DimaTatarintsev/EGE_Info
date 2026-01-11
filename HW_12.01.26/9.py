import csv
from math import prod

def find_max_product(filename='9.csv'):
    max_product = 0
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            nums = list(map(int, row))
            if len(nums) != 7:
                continue
            from collections import Counter
            counter = Counter(nums)
            three_times = [num for num, cnt in counter.items() if cnt == 3]
            if len(three_times) != 1:
                continue
            x = three_times[0]

            others = [num for num in nums if num != x]
            if len(others) != 4:
                continue  
            
    
            if len(set(others)) != 4:
                continue  
            
            if sum(others) > 3 * x:
                continue

            product = prod(others)
            if product > max_product:
                max_product = product
    
    return max_product

if name== 'main':

    print(find_max_product())
