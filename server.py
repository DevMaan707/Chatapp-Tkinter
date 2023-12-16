import socket
import threading
import json
clients=[]
f=[]
def handle_clients(client_):
    data_counter=0
    while True:
            try:
                data=client_.recv(1024).decode('utf-8')
                data_counter+=1
                actual_data=json.loads(data)
                if not data:
                    break
                print(f"RECEIVED DATA FROM {client_} = {actual_data}")
                f.append((actual_data,client_))
                if data_counter==1:
                    pass
                else:
                    for other_clients in clients:
                        if other_clients !=client_:
                            try:
                                #actual_data=(f[0][0],actual_data)
                                other_clients.send(json.dumps(actual_data).encode('utf-8'))
                            except socket.error:
                                pass

            except :
                 pass
    clients.remove(client_)
    client_.close()


def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',3001))

    server.listen(1026)

    client_dict={}
    try:
        while True:
            print("WAITING FOR REQUEST...")
            client_,addr=server.accept()
            print(f"CONNECTION SUCCESSFULL FROM : {client_}")
            clients.append(client_)

            handler=threading.Thread(target=handle_clients,args=(client_,))
            handler.start()
    
    except KeyboardInterrupt:
            print("Server shutting down.")
            server.close()
if __name__=="__main__":
     main()