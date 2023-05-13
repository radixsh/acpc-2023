import sys

FILE = True 
if FILE:
    sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

# https://stackoverflow.com/questions/63343737/how-do-i-take-multi-line-input-from-codeforces
given = sys.stdin.readline().strip()

nums = given.split()
a = int(nums[0])
b = int(nums[1])

final_result = str(a + b)
sys.stdout.write(final_result + "\n")
