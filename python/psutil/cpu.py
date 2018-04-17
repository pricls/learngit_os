#-*- coding=utf-8 -*-
import psutil

#获取CPU信息
print(psutil.cpu_count()) # CPU逻辑数量 非超线程
print(psutil.cpu_count(logical=False))  # CPU物理核心 双核超线程

#统计CPU的用户／系统／空闲时间
print(psutil.cpu_times())

#CPU使用率，每秒刷新一次，累计10次
for x in range(10):
	print(psutil.cpu_percent(interval=1,percpu=True))