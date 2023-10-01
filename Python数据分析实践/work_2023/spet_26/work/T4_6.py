# 输入字符串
input_string = input("请输入一个字符串：")

# 使用字典来存储字符出现次数
char_count = {}

# 统计字符出现次数
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 按出现次数从高到低排序
sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

# 打印排序后的信息
for char, count in sorted_char_count:
    print(f"{char} 字符出现次数为：{count}")
