# 初始化一个空列表来存储所有的买鸡方法
buy_chicken_methods = []

# 遍历大鸡数量（0到20只）
for num_big_chickens in range(21):
    # 遍历中鸡数量（0到33只）
    for num_medium_chickens in range(34):
        # 计算小鸡数量
        num_small_chickens = 100 - num_big_chickens - num_medium_chickens
        # 检查总价是否为100元，并且鸡的总数是100只
        if (
                num_big_chickens * 5 + num_medium_chickens * 3 + num_small_chickens / 3 == 100
                and num_big_chickens + num_medium_chickens + num_small_chickens == 100
        ):
            # 将买鸡方法添加到列表
            buy_chicken_methods.append((num_big_chickens, num_medium_chickens, num_small_chickens))

# 打印所有的买鸡方法
for method in buy_chicken_methods:
    print(f"大鸡: {method[0]}只, 中鸡: {method[1]}只, 小鸡: {method[2]}只")
