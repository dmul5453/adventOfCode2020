inputs = []
numbers = []
answer = 0
target = 2020

with open('inputDay1') as f:
    for line in f:
        inputs.append(line)


print(inputs)
print(len(inputs))

for i in range(len(inputs)):
    numbers.append(int(inputs[i]))

print(numbers)

for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        for k in range(0, len(numbers)):

            if ((numbers[i] + numbers[j] + numbers[k]) == target):
                answer = numbers[i] * numbers[j] * numbers[k]



print(answer)