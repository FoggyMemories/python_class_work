a_list = [4, 10, 12, 4, 9, 6, 3]
b_list = [12, 8, 5, 6, 7, 6, 10]

# 使用集合来删除重复元素并合并列表
c_set = set(a_list + b_list)

# 将集合转换回列表
c_list = list(c_set)

print(c_list)

# 对c_list进行排序
c_list.sort(reverse=True)

print(c_list)
