num = int(input("输入:"))
step = 0
output = str(num)

while num != 1:
    step += 1
    if num % 2 == 0:
        num //= 2
    else:
        num = (num * 3) + 1
    output += f' {num}'

print("输出:", output)
print("步数为:", step)
