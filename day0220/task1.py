from socket import *
sc=socket(AF_INET,SOCK_DGRAM)
addr=("192.168.15.21",8989)
sc.bind(addr)
while True:
    dataencode,caddr=sc.recvfrom(1024)
    datastr=dataencode.decode("utf-8")
    print(datastr)
    sc.sendto("hello".encode(),caddr)
