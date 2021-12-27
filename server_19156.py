import pandas as pd
import socket
df=pd.read_csv('stationary.csv')
print(df)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=6000
host=socket.gethostname()
s.bind((host,port))
s.listen()
print('Server is listening ..')
z=True
c=True
while z:
    con,addr=s.accept()
    print('connection established')
  
    while c:
        data=con.recv(1024)
        f=repr(data.decode())
        print(f)
        f=f[1:]
        f=f[:len(f)-1]
        f=f.split('_')
        print(f)
        
        if f[0]=="I":
            p=f[1:]
            df2=pd.DataFrame.from_records([{'date':p[0],'product_id':int(p[1]),'quantity':int(p[2]),'cost':int(p[3])}])
            print(df2)
            df=pd.concat([df,df2],ignore_index=True)
            print(df)
            df.to_csv('stationary.csv',index=False)
            
        if f[0]=="M":
            df['total_cost']=df['quantity']*df['cost']
            df.to_csv('stationary.csv',index=False)
        if f[0]=="V":
            df.to_csv('k.csv',index=False)
            f_n='k.csv'
            fl = open(f_n,'rb')
            l = fl.read(1024)
            while (l):
               con.send(l)
              
               l = fl.read(1024)
            fl.close()
        if f[0]=='U':
            for i in range(len(df)):
                if df.loc[i,'total_cost']>1000:
                    df.loc[i,'category']='B'
                else:
                    df.loc[i,'category']='A'
            df.to_csv('stationary.csv')
        if f[0]=='F':
            p=f[1:]
            df2=df[df['date']==p[0]]
            k1=str(df2).encode()
            con.send(k1)
        if f[0]=="S":
            con.close()
            c=False
            z=False
            break
    
