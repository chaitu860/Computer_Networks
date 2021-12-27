import socket
import pandas as pd
import csv
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=6000
s.connect((host,port))
print("connected")
s1=0
while s1!='S':
    
    print("Select the actions below")
    print('I-insertion')
    print('M-modify')
    print('V-view')
    print('U-update')
    print('F-view based on pname')
    print('S-stop')
    s1=input()
    if s1=='I':
        date=input('enter date:')
        product_id=input('enter product_id:')
        quantity=input('enter quantity:')
        cost=input('enter pcost:')
        p=str(s1)+'_'+str(date)+'_'+str(product_id)+'_'+str(quantity)+'_'+str(cost)
        
        s.send(p.encode())
        print('sent')
    if s1=='M':
        
        
        p=str(s1)

        p=str(p)
        s.send(p.encode())
        print('modified')
        
    if s1=='V':
       
       
        p=str(s1)
        p=str(p)
        s.send(p.encode())
        print('sent')
        data=s.recv(1024)
        f1=open('m.csv','w')
        f1.write(str(data.decode()))
        f1.close()
        df1=pd.read_csv('m.csv')
        print(df1.loc[:,'date':])
        f2=open('m.csv','r+')
        f2.truncate(0)
        f2.close()
    if s1=='U':
        p=str(s1)
        p=str(p)
        s.send(p.encode())
        print('updated')
    if s1=='F':
        
        
        
        date=input('enter date')
        p=str(s1)+'_'+str(date)
        p=str(p)
        s.send(p.encode())
        print('querying ..')
        m1=s.recv(1024)
        dt=m1.decode()
        print(dt)
    if s1==4:
        break
