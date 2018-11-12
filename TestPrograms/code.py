# FizzBuzz, by Alden Keshap
i = 0
output = ""

while i < 100:
    output = ""
    if not i % 3:
        output = "Fizz"
    if not i % 5:
        output += "Buzz"
    if not output:
        output = i
    print(output)
    i = i + 1
