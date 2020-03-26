#!/usr/bin/python3
# -*- coding: utf-8 -*-

print ("Content-type:text/html")
var = '<html>' \
      '<head>' \
      '<meta charset="GBK">' \
      '<title>Hello Word - 我的第一个 CGI 程序！</title>' \
      '</head>' \
      '<body>' \
      '<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>' \
      '</body>' \
      '</html>'
print ()# 空行，告诉服务器结束头部
# print ('<html>')
# print ('<head>')
# print ('<meta charset="GBK">')
# print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')
# print ('</head>')
# print ('<body>')
# print ('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
# print ('</body>')
# print ('</html>')
print (var)