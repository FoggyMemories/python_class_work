import math


def max_common_divisor_except_self(number):
    if number <= 1:
        return None  # 自然数必须大于1才能计算最大公约数
    max_gcd = 1
    for i in range(2, number):
        if number % i == 0:
            max_gcd = max(max_gcd, math.gcd(number, i))
    return max_gcd


# 测试示例
number = int(input("请输入自然数:"))
result = max_common_divisor_except_self(number)
if result is not None:
    print(f"{number}最大公约数为: {result}")
else:
    print(f"{number}不是一个有效的自然数。")
