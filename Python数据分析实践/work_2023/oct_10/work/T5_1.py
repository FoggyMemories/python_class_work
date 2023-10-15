def print_diamond(n):
    for i in range(1, n + 1):  # 从第一行开始计算*的个数
        if i < n // 2 + 1:  # 如果i行<总行数÷2+1行(最中间那一行)
            star = i * 2 - 1  # 星星的个数
            print(('*' * star).center(n))
        else:
            star = (n - i) * 2 + 1
            print(('*' * star).center(n))


size = int(input("请输入菱形的大小: "))
print_diamond(size)
