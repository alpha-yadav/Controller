import socket as s
import sys
x=s.socket()
x.connect((sys.argv[1],8000))
k=""
while True:
    k=input("$ ").encode()
    x.send(k)
    if(k==b"off"):
        x.close()
        break
    o=x.recv(1024*1024)
    print(o.decode())