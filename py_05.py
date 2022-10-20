#class Cat:
#    def __init__(self,new_name):
#        print("这是初始化方法")
        
#        #self.属性名=属性的初始值
#        #self.name="tom"  #这种就直接将属性固定死了
#        self.name = new_name  #随着参数改变

#    def eat(self):
#        print("%s 爱吃鱼" % self.name)
## 使用类名()创建对象的时候，会自动调用初始化方法__init__
#tom = Cat("tom")
#print(tom.name)

#lazy_cat=Cat("lazy_cat")
#lazy_cat.eat()

#class Cat:
#    def __init__(self,new_name):
#        self.name = new_name
#        print("%s 来了" % self.name)

#    def __del__(self):
#        print("%s 我去了" % self.name)

##tom 是一个全局变量，当整个程序完成之后，系统才会回收tom
##就会自动执行__del__方法。
#tom=Cat("tom")
##print("-" * 50)   #会先输入分割线，再执行__del__

##del 关键字可以删除一个对象
#del tom
#print("-" * 50)    #会先执行__del__，再输入分割线


#class Cat:
#    def __init__(self,new_name):
#        self.name=new_name
#        print("%s 来了" % self.name)

#    def __del__(self):
#        print("%s 走了" % self.name)

#    def __str__(self):
#        #必须返回一个字符串
#        return "我是小猫[%s]" % self.name
    
#tom=Cat("tom")
#print(tom)


## 面向对象封装案例
#class Person:
#    def __init__(self,name,weight):
#        self.name = name
#        self.weight = weight
#    def run(self):
#        self.weight -= 0.5
#    def eat(self):
#        self.weight += 1.0

#xiaoming=Person("xiaoming",75.0)  #自己书写

#class Person:
#    def __init__(self,name,weight):

#        #self.属性=形参
#        self.name = name
#        self.weight = weight

#    def __str__(self):
#        return "我的名字叫 %s 体重是 %.2f 公斤"% (self.name,self.weight)
    
#    def run(self):
#        print("%s 爱跑步，跑步锻炼身体"% self.name)
#        self.weight -= 0.5
#    def eat(self):
#        print("%s 是吃货，吃完这顿再减肥" % self.name)
#        self.weight += 1

#xiaoming = Person("小明",75.0)
#xiaoming.run()
#xiaoming.eat()
#print(xiaoming)    #小明爱跑步教程 v1.0

#class Person:
#    def __init__(self,name,weight):

#        #self.属性=形参
#        self.name = name
#        self.weight = weight

#    def __str__(self):
#        return "我的名字叫 %s 体重是 %.2f 公斤"% (self.name,self.weight)
    
#    def run(self):
#        print("%s 爱跑步，跑步锻炼身体"% self.name)
#        self.weight -= 0.5
#    def eat(self):
#        print("%s 是吃货，吃完这顿再减肥" % self.name)
#        self.weight += 1

#xiaoming = Person("小明",75.0)
#xiaoming.run()
#xiaoming.eat()
#print(xiaoming)    #小明爱跑步教程 v2.0

##小美爱跑步
#xiaomei = Person("小美",45)
#xiaomei.eat()
#xiaomei.run()
#print(xiaomei)


##摆放家具
#class HouseItem:  

#    def __init__(self,name,area):
#        self.name = name 
#        self.area = area 
        
#    def __str__(self):
#        return "[%s] 占地 %.2f"%(self.name,self.area)


#class House:
#    def __init__(self,house_type,area):
#        self.house_type = house_type 
#        self.area = area 

#        #剩余面积
#        self.free_area = area 

#        #家具名称列表
#        self.item_list = []

#    def __str__(self):

#        #python能自动将一对括号内的代码连接在一起
#        return ("户型：%s\n总面积:%.2f[剩余：%.2f]\n家具：%s"
#                %(self.house_type,self.area,
#                  self.free_area,self.item_list))

#    def add_item(self,item):
#        print("要添加 %s" % item)

#        #1.判断家具的面积
#        if item.area > self.free_area:
#            print("%s 的面积太大了，无法添加" % item.name)

#            return
#        #2.将家具的名称添加到列表中
#        self.item_list.append(item.name)

#        #3.计算剩余面积
#        self.free_area -= item.area
    
##1.创建家具
#bed = HouseItem("席梦思",40)
#chest = HouseItem("衣柜",2)
#table = HouseItem("餐桌",20)

#print(bed)
#print(chest)
#print(table)

##2.创建房子对象
#my_home = House("两室一厅",60)
#my_home.add_item(bed)
#my_home.add_item(chest)
#my_home.add_item(table)
#print(my_home)



##士兵突击
#class Gun:
#    def __init__(self,model):

#        #1.子弹的型号
#        self.model = model
#        #2.子弹的数量
#        self.bullet_count = 0

#    def add_bullet(self,count):
#        self.bullet_count += count

#    def shoot(self):
#        #1.判断子弹数量
#        if self.bullet_count <=0:
#            print("[%s] 没有子弹了" % self.model)
#            return 
#        #2.发射子弹-1
#        self.bullet_count -= 1 
#        #3.提示发射信息
#        print("[%s] 突突突 [%d]" % (self.model,self.bullet_count))


#class Soldier:

#    def __init__(self,name): 

#        #1.姓名
#        self.name = name 

#        #2.枪 - 新兵没有枪
#        self.gun = None

#    def fire(self):
#        #1.判断士兵是否有枪
#        if self.gun is None:
#            print("%s 还没有枪"% self.name )
#            return 
#        #2.高喊口号
#        print("冲啊 [%s]" % self.name )

#        #3.让枪装子弹
#        self.gun.add_bullet(50)

#        #4.让枪发射子弹
#        self.gun.shoot()

##1.创建枪对象
#ak47 = Gun("AK47")

##2.创建许三多
#xusanduo = Soldier("许三多")
#xusanduo.gun = ak47
#xusanduo.fire()

#print(xusanduo.gun)



#class Women : 
#    def __init__(self,name) :
#        self.name = name 
#        self.__age = 18 
    
#    def __secret(self) :
#        #在对象的方法内部，是可以访问对象的私有属性的
#        print("%s 的年龄是 %d" % (self.name,self.__age))

#xiaofang = Women("小芳")

##私有属性，在外界不能够被直接访问
##print(xiaofang.__age)

##xiaofang.secret()   #可以执行
#xiaofang.__secret()   #私有方法，同样不允许在外界直接访问



#class Animal:
#    def eat(self):
#        print("吃")
#    def drink(self):
#        print("喝")
#    def run(self):
#        print("跑")
#    def sleep(self):
#        print("睡")
        
#class Dog(Animal):
#    def bark(self):
#        print("汪汪叫")

#class XiaoTianQuan(Dog):  #单继承
#    def fly(self):
#        print("我会飞")

#    def bark(self):       #方法的重写1.直接重新编写方法、实现
#        print("不一样的叫声")

##wangcai = Dog()
##wangcai.eat()
##wangcai.drink()
##wangcai.run()
##wangcai.sleep()
##wangcai.bark()

#xtq = XiaoTianQuan()
#xtq.fly()
#xtq.eat()
#xtq.bark()



#class A:

#    def __init__(self): 
#        self.num1 = 100
#        self.__num2 = 200

#    def __test1(self): 
#        print("私有方法 %d %d "% (self.num1,self.__num2))

#    def test2(self):
#        print("父类的公有方法")
#        self.__test1()
#        print("私有属性 %d" % self.__num2)

#class B(A):

#    def demo(self):

#        #1.在子类的对象方法中，不能访问父类的私有属性
#        #print("访问父类的私有属性 %d"% self.__num2)

#        #2.在子类的对象方法中，不能调用父类的私有方法
#        #self.__test()

#        #间接访问父类的私有属性私有方法
#        self.test2()

#b =B()
#b.demo()



#class A : 
#    def test(self):
#        print("test 方法")

#class B :
#    def demo(self):
#        print("demo 方法")

#class C(A,B) :    #多继承
    
#    pass

##创建子类对象
#c = C()
#c.test()
#c.demo()



#class Dog(object):

#    def __init__(self,name):
#        self.name = name 

#    def game(self):
#        print("%s玩耍"% self.name)

#class XiaoTianQuan(Dog):

#    def game(self):
#        print("%s飞天上玩耍"%self.name)

#class Person(object):

#    def __init__(self,name):
#        self.name = name

#    def game_with_dog(self,dog):
#        print("%s 和 %s 玩耍"%(self.name,dog.name))

#        dog.game()

##1.创建一个狗对象
##wangcai = Dog("旺财")
#wangcai = XiaoTianQuan("飞天旺财")

##2.创建一个小明对象
#xiaoming = Person("小明")

##3.让小明调用和狗玩的方法
#xiaoming.game_with_dog(wangcai)



#"class Tool(object): 

#    #使用赋值语句定义类属性，记录所有工具对象的数量
#    count = 0

#    @classmethod    #类方法
#    def show_tool_count(cls):
#        print("工具对象的数量 %d"%cls.count) 

#    def __init__(self,name):
#        self.name = name
#        Tool.count += 1   #类属性

##1.创建工具对象
#tool1 = Tool("斧头")
#tool2 = Tool("榔头")
#tool3 = Tool("水桶")

##2.输出工具对象的总数
#print(Tool.count)

##调用类方法
#Tool.show_tool_count()



class Dog(object):

    @staticmethod
    def run(): 
        print("小狗要跑")

#通过类名.调用静态方法 - 不需要创建对象
Dog.run()







