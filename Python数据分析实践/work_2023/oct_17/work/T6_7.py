def judge_password():
    try:
        password = input("请输入密码:")
        if int(len(password)) < 8:
            raise IndexError("密码长度不够,请重新输入!")
        else:
            print("输入密码符合规则")
            return password
    except Exception as e:
        print(e)
        judge_password()


judge_password()
