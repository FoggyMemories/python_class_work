def cu_area(length, width=None):
    if width is None:
        # 如果只传递一个参数，将其视为正方形的边长
        width = length

    area = length * width
    perimeter = 2 * (length + width)

    return area, perimeter


# 传递两个参数表示矩形的长和宽
length = 4
width = 3
area, perimeter = cu_area(length, width)
print(f"矩形的面积为：{area}")
print(f"矩形的周长为：{perimeter}")

# 传递一个参数表示正方形的边长
side_length = 5
area, perimeter = cu_area(side_length)
print(f"正方形的面积为：{area}")
print(f"正方形的周长为：{perimeter}")
