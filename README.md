Linux 监控脚本
==========

使用Shell + Python搭建的服务器监控脚本

Shell 负责获取服务器的cpu，内存，磁盘空间的监控，nginx， mysql等应用程序的执行状态

Python 使用 Tornado 提供http接口，供android客户端调用

使用Supervisor 进行 Tornado应用的管理


Feature 0.1
==========

目前实现的比较简单，功能如下
cpu : load avg
memory ： 物理内存使用情况
disk : 磁盘 /  目录使用情况

nginx， mysql， php-fpm, uwsgi, gunicorn 的使用情况


2014-06-27
==========

使用 Flask 重写了服务器端，原因是暂时只想研究一种框架