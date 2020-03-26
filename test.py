#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pip._vendor.distlib.compat import raw_input

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print(counter)
print(miles)
print(name)
print('------------')
a = b = c = 1
print(a)
print(b)
print(c)
print('------------')
a, b, c = 1, 2, "john"

print(a)
print(b)
print(c)
print('------------')
str = 'Hello World!'

print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串
print('------------')
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # 输出完整列表
print(list[0]) # 输出列表的第一个元素
print(list[1:3]) # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表
print('------------')
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

# BOARD_SIZE = 8
#
# def under_attack(col, queens):
#    left = right = col
#    for r, c in reversed(queens):
#  #左右有冲突的位置的列号
#        left, right = left - 1, right + 1
#
#        if c in (left, col, right):
#            return True
#    return False
#
# def solve(n):
#    if n == 0:
#        return [[]]
#
#    smaller_solutions = solve(n - 1)
#
#    return [solution+[(n,i+1)]
#        for i in xrange(BOARD_SIZE)
#            for solution in smaller_solutions
#                if not under_attack(i+1, solution)]
# for answer in solve(BOARD_SIZE):
#    print(answer)

print('------------')
def deduplication(self, nums):  # 找出排序数组的索引
   for i in range(len(nums)):
       if nums[i] == self:
           return i
   i = 0
   for x in nums:
       if self > x:
           i += 1
   return i

print(deduplication(5, [1, 3, 5, 6]))

print('------------')

nums = [11,22,33,44,55,66,77]
even = []
odd = []
while len(nums) > 0:
    num = nums.pop()
    if(num%2 == 0):
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)
print('------------')

for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)


fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")
print('------------')


fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])

print("Good bye!")
print('------------')


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print( num, '是一个质数')
print('------------')


# 定义函数
def printme(int):
    #"打印任何传入的字符串"
    try:
        if int == 1:
            str='123'
        else:
            str = '234'
    except IOError:
        print(IOError)

    else:
        return str


# 调用函数
str = printme(1)
print(str)
str = printme(2)
print(str)

print('------------')


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print( "函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)
print('------------')

# 导入模块
import Comm

# 现在可以调用模块里包含的函数了
var = Comm.print_func("Runoob")
print(var)
print('------------')

# 导入内置math模块
import math

content = dir(math)

print(content)
print('------------')

# 导入 Phone 包
from runoob1 import runoob1
from runoob2 import runoob2

runoob1()
runoob2()
print('------------')

# str = raw_input("请输入：")
# print("你输入的内容是: ", str)
# print('------------')

# 打开一个文件
fo = open("foo.txt", "w")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print( "访问模式 : ", fo.mode)
print('------------')

# 打开一个文件
fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)
print('------------')
# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read()
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()
print('------------')

import os

# 重命名文件test1.txt到test2.txt。
print(os.getcwd())
print('------------')