Web VPython 3.2

sphere(size = vec(10, 10, 10), opacity = 0.3)

ball = []

for i in range(45):

    b = sphere(pos = vector(i * 0.1, i * 0.1, i * 0.1), radius = 0.3)
    print(i + 1)
