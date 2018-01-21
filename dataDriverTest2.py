import csv

# 首先要找到测试用例文件和数据文件的相对位置
# dataDriverTest.py和member_info.csv的相对路径
# 要确定当前dataDriverTest2.py所在的目录
import os
# os 操作系统
# dir是目录的意思
# __file__双下划线开头,双下划线结尾的变量,是python内置的变量
# __file__表示当前文件,这个变量写在那个文件中,就代表哪个文件本身
# C:\Users\51Testing\PycharmProjects\selenium120\data\member_info.csv
# 这时path == C:\Users\51Testing\PycharmProjects\selenium120
# path = os.path.dirname(__file__)
# final_path = path + "\data\member_info.csv"
# print(final_path)
# 这样写代码的好处,就是保证项目在任意路径下都可以执行

# 第二个问题,公用的代码应该封装成一个独立的方法
# def 是define的缩写, 在python中作为方法的关键字
def readData():
    # 多行注释,选中代码后按 ctrl+/
    path = os.path.dirname(__file__)
    final_path = path + "\data\member_info.csv"
    print(final_path)

    # 声明一个空的列表,然后把table中的数据保存到列表中,最后返回列表
    result = []
    # 查看源代码,按住ctrl+鼠标左键
    #file = open(final_path,'r')
    # 在操作系统中打开文件的数量是有限的, 所以每条测试用例都要及时关闭打开的文件
    # 如果程序中间发生异常,那么就会导致关闭失败
    # 所以, 这种情况一般用with语句
    with open(final_path,'r') as file:
        # python中的冒号强大与java中的大括号
        # 遇到冒号,下一行就要缩进4个空格
        # with语句会自动关闭as中生成的对象
        table = csv.reader(file)
        # 这个方法需要有返回值, 有了返回值,测试用例才能操作读取到的数据
        for item in table:
            # print(item)
            result.append(item)
        # file.close()
    return result
abcd = readData()
print(abcd)
print(abcd[0][0])