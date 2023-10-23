def print_triangle():
    print("请输入三角形的三个边")
    a = int(input())
    b = int(input())
    c = int(input())
    try:
        if a + b <= c or a + c <= b or b + c <= a:
            raise Exception("不能够长三角形!")
        else:
            print(f"这是一个边分别为{a},{b},{c}的三角形")
            return
    except Exception as e:
        print(e)


print_triangle()
