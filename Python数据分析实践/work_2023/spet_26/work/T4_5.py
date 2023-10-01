a_list = [4, 8, 7, 8, 6, 3]

# 使用集合来删除重复元素，并将结果排序
unique_numbers = sorted(set(a_list))

# 将排序后的结果连接成字符串
result_string = ''.join(map(str, unique_numbers))

print(result_string)