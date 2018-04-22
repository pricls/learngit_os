import socket # 导入socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建一个socket:
s.connect(('www.sina.com.cn', 80)) # 建立连接
#80端口是Web服务的标准端口 SMTP服务是25端口 FTP服务是21端口

s.send(b'GET / HTTP/1.1\r\nhost: www.sina.com.cn\r\nConnection: clse\r\n\r\n') #发送请求，要求返回首页的内容

buffer = [ ] 
while True:
	d= s.recv(1024) #接收数据 每次最多接收1k字节
	if d:
		buffer.append(d)
	else:  #recv()返回空数据，表示接收完毕，退出循环
		break

date = b''.join(buffer)
s.close()

header, html = date.split(b'\r\n\r\n',1) #把HTTP头和网页分离
print(header.decode('utf-8')) #打印HTTP头文件
# 把接收的数据写入文件
with open('sina.htem','wb') as f:
	f.write(html)