
# Part 1

counter = 0

with open("day_1_D.txt", "r") as file:
    for line in file:
        for char in line:
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1

print(counter)

# Part 2

counter = 0
position = 0

with open("day_1_D.txt", "r") as file:
    for line in file:
        for char in line:
            position += 1
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1

            if counter == -1:
                break

print(position)
