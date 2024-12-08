import os
import time
try:
    import keyboard
except:
    yci = input("计算机内似乎没有安装keyboard库，是否自动安装？(y/n)")
    if yci == "y":
        run_c = os.system("pip install keyboard")
unchoosed = True
print("-")
print("PPC 1.0.2")
print("-")
co = ["1","2"]
while unchoosed:
    print("--------")
    print('''1.暴力纯数字破解
2.暴力数字组合破解''')
    print("--------")
    wa = input("输入功能前的数字来调用：")
    if wa in co:
        unchoosed = False
speed = 0.05
if wa == "1":
    inpass_size = int(input("需要破解的数字密码位数："))
    print("正在准备...")
    pass_size = 10**(inpass_size-1)
    inpass = pass_size
    print(f"破解速度：{speed}个/s")
    print(f"破解将以{pass_size}开始")
    enter = input("#按下Enter以开始#")
    print("注意：请在倒计时结束前将输入焦点定位在要破解的地方")
    time.sleep(2)
    for i in range(5):
        sc = 5 - i
        print(f"将在{sc}秒后开始破解", end='\r')
        time.sleep(1)
    print("破解开始!")
    pass_count = 10**(inpass_size)
    for i in range(pass_count):
        print(f"正在尝试{inpass}",end='\r')
        keyboard.write(str(inpass))
        keyboard.press_and_release("enter")
        inpass += 1
        if inpass > pass_count:
            break
        time.sleep(speed)
elif wa == "2":
    inpass_size = int(input("需要破解的数字密码位数："))
    inpass_h = input("需要破解的数字密码组合的头部(0为空)：")
    if inpass_h == "0":
        inpass_h = ""
    inpass_l = input("需要破解的数字密码组合的尾部(0为空)：")
    if inpass_l == "0":
        inpass_l = ""
    print("正在准备...")
    pass_size = 10**(inpass_size-1)
    inpass = pass_size
    print(f"破解速度：{speed}个/s")
    print(f"破解将以{inpass_h}{pass_size}{inpass_l}开始")
    enter = input("#按下Enter以开始#")
    print("注意：请在倒计时结束前将输入焦点定位在要破解的地方")
    time.sleep(2)
    for i in range(5):
        sc = 5 - i
        print(f"将在{sc}秒后开始破解", end='\r')
        time.sleep(1)
    print("破解开始!")
    pass_count = 10**(inpass_size)
    for i in range(pass_count):
        print(f"正在尝试{inpass_h}{inpass}{inpass_l}",end='\r')
        keyboard.write(str(inpass_h)+str(inpass)+str(inpass_l))
        keyboard.press_and_release("enter")
        inpass += 1
        if inpass > pass_count:
            break
        time.sleep(speed)