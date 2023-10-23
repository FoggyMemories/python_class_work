def print_subtraction():
    a = int(input("请输入第一个数字:"))
    b = int(input("请输入第二个数字:"))
    c = a - b
    try:
        if a < b:
            raise Exception("被减数不能小于减数!")
        else:
            print(f"{a} - {b} = {c}")
    except Exception as e:
        print(e)


print_subtraction()
