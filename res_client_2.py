import socket
import pandas as pd
s=socket.socket()
host=socket.gethostname()
port=6000
s.connect((host,port))
print("WELCOME TO RAILWAY PASSNGER RESERVATION DEPARTMENT")
s1=0
while s1!=4:
    
    print("Select the actions below")
    print('5-view data')
    print('4-stop')
    s1=int(input())
    if s1==5:
        
        p=str(s1)
        
        s.send(p.encode())
        print('sent')
        data=s.recv(1024)
        l=data.decode()
        d=""
        for i in l:
            if i!="\n"  and i!="\r":
                if i==",":
                    d+=" "
                else:
                    d+=i
            elif i=="\n":
                print(d)
                d=""
                
                
        
        
    if s1==4:
        break
