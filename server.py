import socket
import thread
import random
import string
import pandas as pd 
import numpy as np
import sys

# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE, SIG_DFL)

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


print("This is a SERVER program")
print("--------------------------------")

data_type = {
    0: np.byte, #char
    1: np.string_,
    2: np.string_, #binary
    3: np.bool_,
    4: np.int16,
    5: np.double
}

n_col = int(input("Enter number of COLUMNS: "))
n_row = int(input("Enter number of ROWS   : "))

col_type = {}

print("0: char    1: str,    2: binary    3: bool,    4: int,    5: float")

for i in range(n_col):
    # print("Enter column name and datatype")
    nn = input("Enter column name: ")
    dd = int(input("Enter column datatype: "))
    col_type[nn] = data_type[dd]  
    print("")

# nn = input("Enter column name: ")
# dd = int(input("Enter column datatype: "))
# col_type[nn] = data_type[dd]  

# nn = input("Enter column name: ")
# dd = int(input("Enter column datatype: "))
# col_type[nn] = data_type[dd]  

print("Column name and datatype")
print(col_type)

df = pd.DataFrame()

for k, v in col_type.items():
    df[k] = pd.Series(dtype=v)

    if(v == np.byte):
        df[k] = pd.Series(np.array(list(randomString(n_row))))
    elif(v == np.string_):
        l = []
        for i in range(n_row):
            l += [randomString(5)]
        df[k] = pd.Series(np.array(l))
    elif(v == np.bool_):
        df[k] = pd.Series(np.zeros(n_row, dtype=np.bool_))
    elif(v == np.int16):
        df[k] = pd.Series(np.arange(1, n_row+1, 1))
    elif(v == np.double):
        df[k] = pd.Series(np.linspace(0, 2, num=n_row))

print(df)

df.to_csv('File.csv', index=False)

############SOCKET CONNECTION#################
l = []

def on_new_client(clientsocket, addr, df_df, host):
    # while True:
    msg = clientsocket.recv(1024)
    # print(msg," connected")
    print(msg+" connected")
    # print (host, addr, df_df.shape[0])
    # print("")
    f = str(host) + " " + str(addr) + " " + str(df_df.shape[0])
    l.append(f)
    print(l)
    # print(str(host) + " " + str(addr) + " " + str(df_df.shape[0])+"\n")
    # print("")
    try:
        clientsocket.send(df_df.to_string())
    except socket.error:
        pass
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5001                # Reserve a port for your service.
s.listen(50)
log = pd.DataFrame(columns=['Src', 'Des', 'Length', 'Info'])
num_clients = 3
num_rows = n_row//num_clients
start = 0
end = num_rows

print('Server started!')
print('Waiting for clients...\n')

s.bind((host, port))        # Bind to the port
s.listen(5)    

while True:
   c, addr = s.accept()     # Establish connection with client.
   thread.start_new_thread(on_new_client, (c,addr, df[start:end], host))
#    ll = [host, addr, (end-start+1), "Data sent"]
#    log.append(pd.DataFrame(ll), ignore_index = True)
   start = end
   end += num_rows
s.close()
