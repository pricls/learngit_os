#-*- coding=utf-8 -*-
import psutil

# 获取内存信息
v = psutil.virtual_memory()  #物理内存
s = psutil.swap_memory()  #交换内存

# total 总内存大小   used 已用内存大小   percen 占比
print( v ) 
print( s ) 

# 获取磁盘信息
print(psutil.disk_partitions()) # 磁盘分区信息
print(psutil.disk_usage('/')) # 磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO