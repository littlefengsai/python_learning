
#file = open("readme.txt")

#while True :
#    text = file.readline()  #读取一行，向下移动一行文件指针
#    if not text:
#        break

#    #每读取一行的末尾已经有了一个'\n'
#    print(text,end="")

#file.close()



##1.打开
#file_read = open("readme.txt")
#file_write = open("readme[附件].txt","w")

##2.读、写
#text = file_read.read()
#file_write.write(text)

##3.关闭
#file_read.close()
#file_write.close()  #小文件复制



##1.打开
#file_read = open("readme.txt")
#file_write = open("readme[附件].txt","w")

##2.读、写
#while True:
#    text = file_read.readline()
#    #判断是否读取到内容
#    if not text:
#        break
#    file_write.write(text)

##3.关闭
#file_read.close()
#file_write.close()  #大文件复制--一行一行读写



#import os    #os模块的应用（具体看笔记）
#os.rename("readme.txt","README.txt")



#input_str = input("请输入算术题：")
#print(eval(input_str))    #eval函数的应用



#import pygame
#import sys
#print(pygame.ver)   #测试pygame是否安装成功
#if pygame.font is None:
#    print("The font module is not available!")
#    exit()   #测试某些模块在某些平台上不存在



import pygame
print(pygame.examples.aliens)


