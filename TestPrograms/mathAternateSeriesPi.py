import math
total = 0.0
# string = input("Zeros: ")
loops = pow(10, 5)
denom = 1
while denom < loops:
    total += 1.0 / denom
    total -= 1.0 / (denom + 2)
    denom += 4
total *= 4
print(total)
print(abs(total - math.pi))