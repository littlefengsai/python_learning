#i=0
#while i<5:
#    print("hello python")
#    i=i+1


#i=0
#sum=0
#while i<=100:
#    sum+=i
#    i+=1
#print(sum)  #计算0~100的和


#i=0
#sum=0
#while i<=100:
#    if i%2==0:
#        sum+=i
#    i+=1

#print(sum)  #0~100之间所有偶数和


#i=0
#while i<10:
#    if i==3:
#        break
#    print(i)
#    i+=1      #break的用法

#i=0
#while i<10:
#    if i==3:
#        i+=1
#        continue
#    print(i)
#    i+=1




#i=1
#while i<=5:
#    print("*" * i)
#    i+=1       #打印******


#i=1
#while i<=9:
#    j=1
#    while j<=i:
#        sum=0
#        sum=i*j
#        print("%d * %d = %d"%(j,i,sum),end="\t")
#        j+=1
#    i+=1
#    print()   #打印九九乘法表 \t转义字符的应用

    
#def multiple_table():
#    i=1
#    while i<=9:
#        j=1
#        while j<=i:
#            sum=0
#            sum=i*j
#            print("%d * %d = %d"%(j,i,sum),end="\t")
#            j+=1
#        i+=1
#        print()   #定义函数
 
    
#def sum_2_sum(num1,num2):

#    result=num1+num2
#    print("%d + %d = %d"%(num1,num2,result))
#sum_2_sum(50,30)


#def print_line(char,times):
#    print(char * times)

#def print_lines(char,times):
#    row=0
#    while row<5:
#        print_line(char,times)
#        row+=1


#print_lines("=",10)


#name_list=["张三","王五","李四"]
#for my_name in name_list:
#    print("我的名字叫:%s"% my_name)    #迭代遍历的例子  for  in 的应用（与C语言中的for不一样）


#info=[]
#print(type(info))   #空列表
#info=()             #空元组


#info=("小明",18,1.75)
#print("%s 年龄是%d 身高是:%.2f"%info)     

#num_list=[1,2,3]
#num_tuple=tuple(num_list)
#num2_list=list(num_tuple)
#print(type(num_list))
#print(type(num_tuple))
#print(type(num2_list))

#xiaoming={"name":"小明",
#          "age":18,
#          "gender":True,
#          "height":1.75}
#print(xiaoming["name"])

#card_list=[{"name":"zhangsan","qq":"123","phone":"110"},
#           {"name":"lisi","qq":"321","phone":"100"}]
#for card_info in card_list:
#    print(card_info)

#str1="aaaaaa"
#print(str1.count("aa"))

poem = ["登黄鹤楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    print("|%s|"% poem_str.center(10,"*"))


