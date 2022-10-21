
#class Game(object):

#    #历史最高分
#    top_score = 0   #类属性

#    def __init__(self,player_name):    #初始化
#        self.player_name = player_name 

#    @staticmethod   #静态方法
#    def show_help(): 
#        print("帮助信息：让僵尸进入大门")

#    @classmethod    #类方法
#    def show_top_score(cls):
#        print("历史记录 %d"% cls.top_score)

#    def start_game(self):   #实例方法
#        print("%s 开始游戏"% self.player_name)

##1.查看游戏的帮助信息
#Game.show_help()
##2.查看历史最高分
#Game.show_top_score()
##3.创建游戏对象
#game = Game("小明")

#game.start_game()



#class MusicPlayer(object): 
    
#    def __new__(cls,*args,**kwargs):
#        #1.创建对象时，new方法会被自动调用
#        print("创建对象，分配空间")

#        #2.为对象分配空间
#        instance = super().__new__(cls)

#        #3.返回对象的引用
#        return instance 

#    def __init__(self):
#        print("播放器初始化")
        

#player = MusicPlayer()

#print(player)



#class MusicPlayer(object):

#    #记录第一个被创建对象的引用
#    instance = None

#    #记录是否执行过初始化方法
#    init_flag = False

#    def __new__(cls,*args,**kwargs):   #单例的设置
#        #1.判断类属性是否是空对象
#        if cls.instance is None:
#            #2.调用父类的方法，为第一个对象分配空间
#            cls.instance = super().__new__(cls)
#        #3.返回雷属性保存的对象引用
#        return cls.instance

#    def __init__(self):     #只执行依次的初始化设置
        
#        #1.判断是否执行过初始化方法
#        if MusicPlayer.init_flag :
#        #2.如果没有执行过，在执行初始化动作
#            return 
#        print("初始化播放器")

#        #3.修改类属性的标记
#        MusicPlayer.init_flag = True

##创建多个对象
#player1 = MusicPlayer()
#print(player1)

#player2 = MusicPlayer()
#print(player2)   #两个player内存地址一样。



#try:
#    #不能确定正确执行的代码
#    num = int(input("请输入一个整数:"))
#except:
#    #错误的处理代码
#    print("请输入正确的整数")

#print("-" * 50)

#try : 
#    #提示用户输入一个整数
#    num = int(input("请输入一个整数："))

#    #使用 8  除以用户输入的整数并输出
#    result = 8 / num 

#    print(result)
#except ZeroDivisionError :
#    print("除0错误")
#except ValueError :
#    print("请输入正确的整数")
#except Exception as result :
#    print("未知错误 %s" % result)
#else :
#    print("尝试成功")
#finally :
#    print("无论是否出现错误都会执行的代码")


#def demo1():
#    return int(input("请输入一个整数："))

#def demo2():
#    return demo1()

## 利用异常的传递性，在主程序捕获异常
#try :
#    print(demo2())
#except Exception as result:
#    print("未知错误 %s" % result)


#def input_password():
#    #1.提示用户输入密码
#    pwd = input("请输入密码:")
#    #2.判断密码长度>=8，返回用户输入的密码
#    if len(pwd)>=8:
#        return pwd
#    #3.如果<8主动抛出异常
#    print("主动抛出异常")
#    #1>创建异常对象
#    ex = Exception("密码长度不够")

#    #2>主动抛出异常
#    raise ex

##提示用户输入密码
#try :
#    print(input_password())
#except Exception as result:  #捕获(未知)异常 - 这里捕获的是主动抛出的异常
#    print(result)

file = open("readme.txt")

text = file.read()
print(text)

file.close()










