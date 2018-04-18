#-*- coding=utf-8 -*-
import psutil

# 获取进程信息
print('所有进程ID:')
print(psutil.pids()) #所有进程ID
p = psutil.Process(2289) #获取指定进程ID=3776
print('2289进程名称(p.name):')
print(p.name())
print('2289进程exe路径(p.exe):')
print(p.exe())
print('进程工作目录(p.cwd):')
print(p.cwd())
print('进程启动的命令行(p.comline)')
print(p.cmdline())
print('父进程ID(p.ppid):')
print(p.ppid())
print('父进程(p.parent):')
print(p.parent())
print('子进程列表(p.children):')
print(p.children())
print('进程状态(p.status()')
print(p.status())
print('进程用户名(p.username):')
print(p.username)
print('进程创建时间(p.create_time):')
print(p.create_time)
print('进程终端(p.terminal):')
print(p.terminal())
print('进程使用的CPU时间(p.cpu_times):')
print(p.cpu_times())
print('进程使用的内存(p.memory_info):')
print(p.memory_info())
print('进程打开的文件(p.open_files):')
print(p.open_files())
print('进程相关网络连接(p.connections):')
print(p.connections())
print('进程的线程数量(p.num_threads):')
print(p.num_threads())
print('所有线程信息(p.threads):')
print(p.threads())
print('进程环境变量(p.environ):')
print(p.environ())
print('结束进程:p.terminate()')