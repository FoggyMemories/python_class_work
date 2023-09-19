def prime_factors(n):
    factors = []  # 用于存储质因数的列表
    divisor = 2  # 初始除数

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


# 输入要分解的正整数
number = int(input("请输入一个整数："))

if number <= 0:
    print("请输入一个有效的正整数。")
else:
    factors = prime_factors(number)
    if len(factors) == 1:
        print(f"{number}是一个质数，没有其他质因数。")
    else:
        factors_str = ' * '.join(map(str, factors))
        print(f"{number} = {factors_str}")
