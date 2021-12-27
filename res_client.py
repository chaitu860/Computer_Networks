import socket
s=socket.socket()
host=socket.gethostname()
port=6000
s.connect((host,port))
print("WELCOME TO RAILWAY PASSNGER RESERVATION DEPARTMENT")
s1=0
while s1!=4:
    
    print("Select the actions below")
    print('1-add_info')
    print('2-update_info')
    print('3-get_info')
    print('4-stop')
    s1=int(input())
    if s1==1:
        train_id=input('enter train id:')
        train=input('enter train name:')
        sleeper=input('enter number of passengers in sleeper:')
        ac3=input('enter no of passengers in 3A:')
        ac2=input('enter no of passengers in 2A:')
        p=str(s1)+'_'+str(train_id)+'_'+str(train)+'_'+str(sleeper)+'_'+str(ac3)+'_'+str(ac2)
        
        s.send(p.encode())
        print('sent')
    if s1==2:
        
        train_id=input('enter train id:')
        sleeper=input('enter class(sleeper/3a/2a:')
        num=input('enter no of passengers to update:')
        p=str(s1)+'_'+str(train_id)+'_'+str(sleeper)+'_'+str(num)

        p=str(p)
        s.send(p.encode())
        print('updated')
        
    if s1==3:
        train=input('enter train id:')
        sleeper=input('enter class(sleeper/3a/2a:')
    
       
        p=str(s1)+'_'+str(train)+'_'+str(sleeper)
        p=str(p)
        s.send(p.encode())
        print('sent')
        data=s.recv(1024)
        print('no of pasengers are',data.decode())
    if s1==4:
        break
