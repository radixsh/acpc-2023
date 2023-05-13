import sys

# FILE = True 
# if FILE:
#     sys.stdin = open('input.txt', 'r')
#     # sys.stdout = open('output.txt', 'w')

# https://stackoverflow.com/questions/63343737/how-do-i-take-multi-line-input-from-codeforces
given = sys.stdin.readline().strip()
nums = given.split()
n = int(nums[0])
k = int(nums[1])

drinks = sys.stdin.readline().strip().split()
drinks = list(map(int, drinks))
# https://stackoverflow.com/questions/43432675/sort-a-list-in-reverse-order
# drinks = sorted(drinks, reverse=True)

# https://www.geeksforgeeks.org/insertion-sort/# 
for i in range(1, n):
    key = drinks[i]
    j = i - 1
    while j >= 0 and drinks[j] < key:
        drinks[j + 1] = drinks[j]
        j -= 1
    drinks[j + 1] = key

# print(drinks)

# for i in range(0, n) :
#     for j in range(0, n-1):
#         if drinks[j] < drinks[j+1]:
#             temp = drinks[j]
#             drinks[j] = drinks[j+1]
#             drinks[j+1] = temp

max_caffeine = 0
output_list = []
for i in range(0, k):
    max_caffeine += drinks[i]
    output_list.insert(0, drinks[i])

sys.stdout.write(str(max_caffeine) + "\n")
sys.stdout.write(' '.join(str(e) for e in output_list) + "\n")
