sum = 0
i = 0
while i < 10:
    if i % 4 == 0:
        continue
    sum += i
    i += 1
print(sum)
