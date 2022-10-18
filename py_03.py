##要求：
##1.将字符串中的空白字符全部去掉
##2.再使用“ ”作为分隔符，拼接成一个整齐的字符串
#poem_str="登鹳雀楼\t 王之涣\t 白日依山尽\t \n 黄河入海流 \t \t欲穷千里目\t \n更上一层楼"
#print(poem_str)

##1.拆分字符串
#poem_list=poem_str.split()
#print(poem_list)  #split用法：将空格符去掉；拆分成一个个的小字符串，返回一个列表

##2.合并字符串
#poem_str1=  " ".join(poem_list)   #join的用法：用分隔符将字符串串联起来。返回一个字符串
#print(poem_str1)

#num_str="0123456789"
#print(num_str[2:6])  #截取从2--5位置的字符串
#print(num_str[2:])  #截取从2--末尾的字符串
#print(num_str[:6])  #截取从开始--5位置的字符串
#print(num_str[:])  #截取完整的字符串
#print(num_str[::2])  #从开始位置，每隔一个字符截取字符串
#print(num_str[1::2])  #从索引1开始，每隔一个取一个
#print(num_str[2:-1])  #截取从2--末尾-1的字符串
#print(num_str[-2:])  #截取字符串末尾两个字符
#print(num_str[-1::-1])  #字符串的逆序
#print(num_str[::-1])  #字符串的逆序

#students =[{"name":"xiaomei"},{"name":"atu"}]
#find_name="lisi"
#for stu_dict in students:
#    print(stu_dict)
#    if stu_dict["name"]==find_name:
#        print("find %s" % find_name)
#        break
#else:
#    print("sorry,not find:%s" % find_name)
#print("circul over")

def measure():
    temp=39
    wetness=50

    return [temp,wetness]

result=measure()
print(result)
