from collections import Counter

a_list = [4, 5, 8, 6, 4, 2, 6, 6, 5, 7, 4, 2, 1, 7, 6, 7, 4]

# 使用Counter统计元素个数
element_counts = Counter(a_list)

# 输出统计结果
for element, count in element_counts.items():
    print(f"元素 {element} 在列表中出现 {count} 次")
