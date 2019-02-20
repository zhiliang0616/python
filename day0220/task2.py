from socket import *
sc=socket(AF_INET,SOCK_DGRAM)
while True:
    sc.sendto("hi".encode(),('192.168.15.21',8989))
    receivecode,saddr = sc.recvfrom(1024)
    receivedata=receivecode.decode(encoding="utf-8")
    print(receivedata)
