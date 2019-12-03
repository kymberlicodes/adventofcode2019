import math

sum = 0

def func(mass, sum):
    print(mass, sum)
    mass = math.floor(mass / 3) - 2
    sum += mass
    print("this is the sum", sum)

try:
    file = open("input.txt", "r")
    mass = file.readlines()
    func(int(mass[0]), sum)
    print(sum)
finally:
    file.close()