while True:
    try:
        num = int(input("请输入一个整数："))
    except ValueError:
        print("输入不符合要求，请重新输入！")
    else:
        print("输入正确，你输入的整数为：", num)
        break
