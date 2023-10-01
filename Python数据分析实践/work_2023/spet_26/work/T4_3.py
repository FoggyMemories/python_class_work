# 初始化一个空列表来存储符合要求的三位数
result = []

# 遍历百位数字
for hundreds in [4, 6, 8, 9]:
    # 遍历十位数字
    for tens in [4, 6, 8, 9]:
        # 遍历个位数字
        for ones in [4, 6, 8, 9]:
            # 检查百、十、个位数字都不相同
            if hundreds != tens and tens != ones and ones != hundreds:
                # 计算三位数并添加到结果列表
                number = hundreds * 100 + tens * 10 + ones
                result.append(number)

# 打印符合要求的三位数列表
print(result)
