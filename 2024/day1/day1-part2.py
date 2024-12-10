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

# sum = 0
# for i in range(1000):
#     sum += abs(list1[i] - list2[i])
#
# print(sum)

number_occurrence_map = {}
similarity_score = 0
for num in list2:
    if num not in number_occurrence_map:
        number_occurrence_map[num] = 1
    else:
        current_count = number_occurrence_map[num]
        number_occurrence_map[num] = current_count + 1

for num in list1:
    if num in number_occurrence_map:
        count = num * number_occurrence_map[num]
        similarity_score += count

print(similarity_score)
