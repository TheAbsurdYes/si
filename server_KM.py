import base64
import socket

from Crypto.Util.py3compat import tostr
from functii import *
from base64 import b64encode

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2)
    conn_a, address_a = server_socket.accept()  # accept new connection
    conn_b, address_b = server_socket.accept()  # accept new connection
    
    print("Connection from: " + str(address_a))
    print("Connection from: " + str(address_b))
    
    
    data = conn_a.recv(1024).decode()

    K = get_random_bytes(16)
    K_prim = str(data.split()[1]) # parola
    operare = str(data.split()[0]) # modul de operare

    if operare == 'ECB':
        K = ecb_encrypt(K,K_prim,16)
    elif operare == 'CFB':
        IV = get_random_bytes(16)
        K =  cfb_encrypt(K,K_prim,16,IV)


    conn_b.send(K,operare,K_prim)


    conn_a.close()  # close the connection
    conn_b.close()  # close the connection


if __name__ == '__main__':
    server_program()
