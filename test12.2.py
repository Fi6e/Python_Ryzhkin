from math import cos, sin

class Star:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def rotate(self, angle):
        x1, y1 = self.x, self.y

        self.x = cos(angle) * x1 - sin(angle) * y1
        self.y = sin(angle) * x1 + cos(angle) * y1



with open("input.txt") as input_file:
    first_line = input_file.readline().split()
    N = int(first_line[0])
    angle = int(first_line[1])

    stars = []
    for i in range(N):
        line = input_file.readline().split()
        name = line[0]
        x, y = float(line[1]), float(line[2])

        stars.append(Star(name, x, y))

        stars[i].rotate(angle)

stars.sort(key = lambda star: star.y)

with open("output.txt", "w") as output_file:
    for star in stars:
        output_file.write(star.name + " ")
    output_file.write("\n")
    
    