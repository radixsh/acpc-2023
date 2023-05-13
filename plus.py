import sys
from os import path

FILE = True 
if FILE:
    sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def outward(text):
    sys.stdout.write(text + "\n")

# https://stackoverflow.com/questions/63343737/how-do-i-take-multi-line-input-from-codeforces
given = get_string()
outward("Input: " + given)

''' 
BEGIN ALGORITHM 
'''

nums = given.split()
a = int(nums[0])
b = int(nums[1])

final_result = str(a + b)

''' 
END ALGORITHM 
'''

outward("Output: " + final_result)
