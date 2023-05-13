import sys

FILE = True 
if FILE:
    sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')


def max_val(array):
    A, B, C, D = array
    first = 0

    if A == C:
        first = A + C
    elif A == 0:
        first = C
    else:
        first = -1
   
    second = 0
    if B == D:
        second = B + D
    elif B == 0:
        second = D
    else:
        second = -1

    return max(first, second)



# https://stackoverflow.com/questions/63343737/how-do-i-take-multi-line-input-from-codeforces
first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

a, b = first.split()
a = int(a)
b = int(b)
c, d = second.split()
c = int(c)
d = int(d)

nums = list(map(int, [a, b, c, d]))

if all(n == 0 for n in nums):
    sys.stdout.write("0\nup\n")
    exit(0)

arrays = [
        [a,b,c,d],   # up
        [c,a,d,b],   # left 
        [b,d,a,c],   # right
        [d,c,b,a]    # down
        ]

candidates = {}
candidates["up"] = int(max_val(arrays[0]))
candidates["left"] = int(max_val(arrays[1]))
candidates["right"] = int(max_val(arrays[2]))
candidates["down"] = int(max_val(arrays[3]))
# print(candidates)

direction = ""
greatest = 0
for key, value in candidates.items():
    if value > greatest:
        direction = key
        greatest = value

sys.stdout.write(str(greatest) + "\n")
sys.stdout.write(direction + "\n")
