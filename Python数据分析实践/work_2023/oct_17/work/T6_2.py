while True:
    try:
        arrList = [int(j) for j in input("请连续输入五个整数:").split("、")]
        for i in range(5):
            print(arrList[i])
    except ValueError:
        print("请输入整数")
    except IndexError:
        print("请输入至少5个整数！")
    else:
        break
