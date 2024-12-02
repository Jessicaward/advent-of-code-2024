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

similarity_score = 0

for location in list1:
    num_times_location_appears = sum(1 for l in list2 if l == location)
    similarity_score = similarity_score + (int(location) * num_times_location_appears)

print(similarity_score)