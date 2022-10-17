# 定义苹果单价
#price=8.5
# 挑选苹果
#weight=7.5
# 计算金额
#money= price * weight
# 只要买苹果就返5元
#moeny = money - 5
#print(moeny)


#age = int(input("请输入年龄"))
#if age >=18 :
#    print("你已经成年")
#else :
#    print("你还未成年")


#age = int(input("请输入年龄"))
#if (age>=0 and age<= 120):
#    print("年龄正确")
#else :
#    print("年龄不正确")  #and运算符的应用


#python_score=8
#c_score=7
#if(python_score>60 or c_score>60):
#    print("考试通过")
#else:
#    print("考试失败,继续努力")  #or运算符的应用


#is_employee=True
#if not is_employee:
#    print("非本公司成员，禁止入内")  #not运算符的应用


#holiday_name = "情人节"
#if holiday_name == "情人节":
#    print("买玫瑰")
#    print("看电影")
#elif holiday_name == "平安夜":
#    print("买苹果")
#    print("吃大餐")
#elif holiday_name == "生日":
#    print("买蛋糕")

#else:
#    print("每天都是节日啊")   #elif的应用


has_ticket=True
knife_length=30
if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length>20:
        print("携带危险物品，不允许上车")
    else:
        print("安检通过，祝你旅途愉快")
else:
    print("大哥请先买票")