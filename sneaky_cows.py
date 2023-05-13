import sys

# FILE = True 
# if FILE:
#     sys.stdin = open('input.txt', 'r')
#     # sys.stdout = open('output.txt', 'w')

# https://stackoverflow.com/questions/63343737/how-do-i-take-multi-line-input-from-codeforces
s = sys.stdin.readline().strip()
length = len(s)

num_cows = 0 #potential_cows.count('cow')
indices_of_cows = []

for i in range(1, (length - 3)):
    # print(s[i:i+3])
    if s[i:i+3] == "cow":
        num_cows += 1
        indices_of_cows.append(i)
# print(num_cows)

# print(indices_of_cows)
for index in indices_of_cows:
    if s[index+3:index+6] == "cow" or s[index-3:index] == "cow":
        # print("before: " + s[index-3:index])
        # print("after: " + s[index+3:index+6])
        num_cows -= 1

sys.stdout.write(str(num_cows))


# for letter in s.split():
#     cur = 1
#     while cur < len(s):
# 
#         if 

# final_result = str(a + b)
# sys.stdout.write(final_result + "\n")
