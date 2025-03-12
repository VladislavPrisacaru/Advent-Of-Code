
# Part 1

ribbon = 0
result = 0
with open("day_2_D.txt", "r") as file:
    data = file.readlines()
    
    for line in data:
        length, width, heigth = map(int,line.split("x"))
        d1 = 2 * length * width
        d2 = 2 * width * heigth
        d3 = 2 * heigth * length
        smallest = min(d1, d2, d3)
        result += d1 + d2 + d3 + (smallest/2)

        # Part 2
        smallest_r = min(2* (length + width), 2* (width + heigth), 2* (heigth + length))
        ribbon += (smallest_r) + (length * width * heigth)
         


print(result)
print(ribbon)


