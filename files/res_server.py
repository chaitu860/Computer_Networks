import socket
import threading
import pandas as pd
df=pd.read_csv('train_list.csv')
df=df.set_index('train_id')
print(df)
s=socket.socket()
port=6000
host=socket.gethostname()
s.bind((host,port))
s.listen()
print('Server is listening ...Passenger_Reservation__Department')

   
def add_info(p,df):
  
    df2=pd.DataFrame.from_records([{'train':p[0],'sleeper':int(p[1]),'3a':int(p[2]),'2a':int(p[3])}],index='train_')
    print(df2)
    df=df.append(df2)
    print(df)
    df.to_csv('train_list.csv')
def handle_client(con,df,adr):
    c=True
    while c:
        data=con.recv(1024)
        f=repr(data.decode())
        print(f)
        f=f[1:]
        f=f[:len(f)-1]
        f=f.split('_')
        print(f)
        
        if f[0]=="1":
            p=f[1:]
            df2=pd.DataFrame.from_records([{'train_id':p[0],'train':p[1],'sleeper':int(p[2]),'3a':int(p[3]),'2a':int(p[4])}],index='train_id')
            print(df2)
            df=df.append(df2)
            print(df)
            df.to_csv('train_list.csv')
            
        if f[0]=="2":
            p=f[1:]
            df.at[int(p[0]),p[1]]=p[2]
            
        if f[0]=="3":
            d=get_info(f[1:],df)
            print(d)
            con.send(str(d).encode())
          
        if f[0]=="4":
            c=False
        if f[0]=="5":
            dfi=str(df)
            con.send(dfi.encode())
    con.close()
def get_info(p,df):
    id=df.index
    if  (p[1] not in df):
        return 'Not exist'
    return df.at[int(p[0]),p[1]]
while True:
    
    con,addr=s.accept()
    print('Connection established from ',addr)
    thread=threading.Thread(target=handle_client,args=(con,df,addr))
    thread.start()
    
    
       
