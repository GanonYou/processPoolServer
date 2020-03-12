#!/usr/bin/python
#coding:utf-8
import sys,os
length = os.getenv('CONTENT_LENGTH')
 
if length:
    postdata = sys.stdin.read(int(length))
    print("Content-type:text/html\n")
    print('<html>')
    print('<head>')
    print('<title>Info</title>')
    print('</head>')
    print('<body>')
    print('<h1> Your register information is: </h1>')
    print('<ul>')
    for data in postdata.split('&'):
        tmp = ""
        for i in range(len(data)):
            if data[i] == "+":
                tmp += " "
            elif data[i] == "=":
                tmp += " : "
            else:
                tmp += data[i]
        print('<li>' + tmp + '</li>')
    print('</ul>')
    print('</body>')
    print('</html>')
     
else:
    print("Content-type:text/html\n")
    print('no found')