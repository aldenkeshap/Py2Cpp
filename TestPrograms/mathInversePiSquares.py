import math
total = 0.0
# string = input("How many zeros? ")
end = 5
end = pow(10, end)
piSquared = pow(math.pi, 2)
for i in range(1, end + 1):
    total += 1 / (piSquared * pow(i, 2) + 1)

print(total)
total = 1 / total
total += 1
total = math.sqrt(total)
print(total)
print(abs(total - math.e)) 
print('Hello')