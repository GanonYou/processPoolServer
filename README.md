# processPoolServer

进程池版Web服务器，使用C++开发，能够处理浏览器的GET/POST请求并做出响应

环境: Parallels Desktop下安装的ubuntu 16.04LTS

## Quick Start

1. 将html目录下的cgi程序勾选可执行权限

2. make，并启动服务器监听相应端口
```
cd processPoolServer
make
./cgi_server 127.0.0.1 8888
```

3. 打开浏览器，访问127.0.0.1 8888
![visit1](https://github.com/GanonYou/processPoolServer/blob/master/example/visit1.png)

4. 填写表单后submit
![return](https://github.com/GanonYou/processPoolServer/blob/master/example/return.png)

## 进程池结构

![pool](https://github.com/GanonYou/processPoolServer/blob/master/example/pool.png)

1.父进程负责监听listenfd上的新连接，监听到新连接请求使用Round Robin轮询调度子进程通知，子进程负责处理客户端的请求(需要借助CGI)

2.父进程和子进程之前的通信方式选择管道，因为管道有文件描述符，可以使用epoll的IO多路复用功能

- 父进程和**每个**子进程之间都有一个处理新连接请求的管道m_pipefd
- 信号事件转化为一个全局管道sig_pipefd的读写处理,信号处理函数向管道中写,父进程和子进程从管道中读,需要将写入端sig_pipe[1]设置为非阻塞
- 父进程的epollfd,负责监听listenfd以及信号事件
- 子进程的epollfd,负责监听与父进程的管道读端以及信号事件


## CGI

1. 子进程本身可以处理客户端的GET请求，默认访问register.html

2. 若为客户端POST请求，则需要执行相应的CGI程序register.cgi

服务器CGI的调用可以参考下图

![cgi](https://github.com/GanonYou/processPoolServer/blob/master/example/cgi.png)


