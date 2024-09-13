import os
import webbrowser as w
import socket as s
file_Pdir=__file__.split("/")
path=""
for i in range(1,len(file_Pdir)-1):
    path+=file_Pdir[i]+"/"
print(path)
with open(path+"result.log","w") as k:
    pass
x=s.socket()
x.bind(("ADITYADAV",8000))
x.listen(3)
print(s.gethostbyname("ADITYADAV"))
for mk in range(1000):
 a,b=x.accept()
 i=" "
 print(b)
 py_cmd={"cd":os.chdir}
#,"mkdir":os.makedirs,"mv","rmdir","cp"]
 while True:
    try:
        i=a.recv(1024*1024).decode()
    except:
        i="off"
    #if(i.isalpha()):
    if(i=="off"):
        a.close()
        break
    j=''
    if("run" in i):
        z=i.split("run ")
        for k in range(1,len(z)):
            j+=z[k]
        print(k)
        z=w.open(j)
        a.send(str(z).encode())
    elif("cd "  in i):
        z=i.split("cd ")
        for k in range(1,len(z)):
            j+=z[k]
        try:
            py_cmd["cd"](j)
            a.send(b"-")
        except:
            a.send(b"FileNotFoundError")
#            print(FileNotFoundError())
            #a.send(FileNotFoundError.encode())
    else:
        os.system(i+" >"+path+"result.log 2>&1")
        k=open(path+"result.log","rb") #,open("error.log","rb")]
        m=k.read()
        a.sendall(m)
        k.close()
    #os.remove(k.name)