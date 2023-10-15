def sumN(s1, s2):
    sum = 0
    if s1 > s2:
        max = s1
        min = s2
    else:
        max = s2
        min = s1
    for i in range(min, max + 1):
        sum += i
    return sum


print(sumN(12, 1))
print(sumN(12, 123))
