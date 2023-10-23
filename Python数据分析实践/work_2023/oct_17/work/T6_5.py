def judge_score():
    num = float(input("请输入分数:"))
    try:
        if num < 0 or num > 100:
            raise Exception("分数必须在 0 ~ 100 之间!")
    except Exception as e:
        print(e)
        judge_score()
    else:
        print("成绩格式正确")


judge_score()
