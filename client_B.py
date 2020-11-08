import socket
from functii import *

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

    K = data.split()[0] #cheia criptate de la A
    operare = data.split()[1] # modul de operare
    K_prim = data.split()[2] # cheia prim
    
    if operare == 'ECB':
        K = ecb_decrypt(K,16)
    elif operare == 'CFB':
        IV = get_random_bytes(16)
        K =  cfb_decrypt(K,16,IV)

    print('')

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()