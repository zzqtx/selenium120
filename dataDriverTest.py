# 数据驱动测试,首先要读取数据文件
# 数据文件类型:
# 数据库,excel(手工操作常用excel比较多),csv(是excel的一种),txt
# 如何读取csv文件中的数据?
# 1.首先准备一个csv文档
# 2.要想读取csv文件,必须引入csv的代码库
import csv
# 3.必须知道文件的目录结构
# 复制文件路径 C:\Users\51Testing\PycharmProjects\selenium120\data\member_info.csv
# 程序里的代码,不能用绝对路径,应该改成相对路径,这样便于多人协同工作
path= r"C:\Users\51Testing\PycharmProjects\selenium120\data\member_info.csv"
# 记录路径的三种方法:
# 字符串前面加r,(这种方法书写最简单)
# 反斜线变成正斜杠,才能跨平台
# 反斜线改成双反斜线
# 4.打开member_info.csv文件
file = open(path,'r')
# 5.因为文件中的内容属于csv格式,需要用csv中的read方法读取其中内容
table = csv.reader(file)
# 6.用for循环读取数据
# 把table中每一行取出,作为item的值,然后我们打印每一行
for item in table:
    print(item)