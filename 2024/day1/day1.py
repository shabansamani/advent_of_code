"""
Steps:
1. Take in input
2. Sort both lists
3. Pair the numbers up in both lists by indices
4. Calculate absolute difference
5. Sum of absolute differences
"""

with open("input.txt", "r") as file:
    lines = file.readlines()
list1 = []
list2 = []
for line in lines:
    data = line.split()
    list1.append(int(data[0]))
    list2.append(int(data[1]))

list1.sort()
list2.sort()
sum = 0
for i in range(1000):
    sum += abs(list1[i] - list2[i])

print(sum)
