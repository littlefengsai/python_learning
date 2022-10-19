## 不使用其他变量，交换两个变量的值
## python特有的解法
#a=6
#b=100
#a,b=b,a

#a=a+b
#b=a-b
#a=a-b  #常规解法

#def demo(num):
#    print("函数内部的代码")
#    # 在函数内部，针对参数使用赋值语句,不会修改到外部的实参变量
#    num=100

#    print(num)

#gl_num=99
#demo(gl_num)
#print(gl_num)

#def demo(num_list):
#    num_list.append(9) # 使用方法修改列表内的内容
#    print(num_list)

#gl_list=[1,2,3]
#demo(gl_list)
#print(gl_list)

#def print_info(nam,gender=True):
#    gender_text="男生"
    
#    if not gender:
#        gender_text="女生"

#        print("%s是%s"%(name,gender_text))

#print_info("小明")  #因为没有传入性别所以执行默认值
#print_info("小美",False)

#def print_info(num,num_tuple,num_dict,num_list):
#    print(num,yuanzu,num_dict,num_list)

#num=1
#num_tuple=(1,2,3)
#num_dict={"姓名":1,"学号":2,"年龄":3}
#num_list=[1,2,3]
#print_info(num,num_tuple,num_dict,num_list) #变量之间的传参

#def demo(num,*nums,**person):
#    print(num)
#    print(nums)
#    print(person)
    
#demo(1,2,3,4,5,name="小明",age=18)  #直接传递数据的传参


#def sum_numbers(*args):
#    num=0
#    print(args)

#    for n in args:
#        num+=n

#    return num

#result =sum_numbers(1,2,3,4,5)
#print(result)    


#def sum_numbers1(num):
#    if num==1:
#        return 1
#    temp=sum_numbers1(num-1)+num
#    return temp   #递归自己书写

#def sum_numbers2(num):
#    if num==1:
#        return 1
#    temp=sum_numbers2(num-1)
#    return num+temp   #递归教程

#result1=sum_numbers1(5)
#print(result1)
#result2=sum_numbers2(3)
#print(result2)


#class Cat:       #猫类
#    def eat(self):
#        print("小猫爱吃鱼")
#    def drink(self):
#        print("小猫爱喝水")
        
#tom=Cat()     #由猫类创建的tom对象
#tom.eat()
#tom.drink()   #面向对象的程序


class Cat:       #猫类
    def eat(self):
        print("%s爱吃鱼"%self.name)
    def drink(self):
        print("%s爱喝水"%self.name)
        
tom=Cat()     #由猫类创建的tom对象
tom.name="tom"
tom.eat()
tom.drink()   #面向对象的程序

lazy_cat=Cat()   #再创建一个猫对象
lazy_cat.name="lazy_cat"
lazy_cat.eat()
lazy_cat.drink()

