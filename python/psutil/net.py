#-*- coding=utf-8 -*-
import psutil

# 获取网络信息
netio = psutil.net_io_counters() #获取网络读写字节／包的个数
print('网络读写字节／包的个数:')
print(netio)

netifa = psutil.net_if_addrs() #获取网络接口信息
print('网络接口信息:')
print(netifa)

netifs = psutil.net_if_stats() #获取网络接口状态
print('网络接口状态:')
print(netifs)

netc = psutil.net_connections() #获取当前网络连接信息
print('当前网络连接信息:')
print(netc)
