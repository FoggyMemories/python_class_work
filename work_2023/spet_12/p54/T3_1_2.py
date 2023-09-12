sum = 0
for i in range(10):
    if i // 4 == 2:
        continue
    sum += i
print(sum)
