list1 = []
list2 = []

def build_lists(filename: str):
    with open(filename) as f:
        lines = f.read().splitlines()

    for line in lines:
        split = line.split("   ")
        list1.append(split[0])
        list2.append(split[1])

build_lists("input.txt")

list1.sort()
list2.sort()

# We essentially have to build this list based on how far apart each number is, so we need the absolute difference
difference_list = []

for index in range(0, len(list1)):
    absolute_difference = abs(int(list1[index])-int(list2[index]))
    difference_list.append(absolute_difference)

total_difference = sum(difference_list)

print(total_difference)