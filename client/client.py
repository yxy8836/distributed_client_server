#!/usr/bin/env python

import sys
import socket as sk

if __name__=='__main__':

    send=True
    # check input argument for send or receive mode
    if sys.argv[3]=='receive':
        send=False
    elif sys.argv[3]=='send':
        file = sys.argv[4]
        send=True
    else:
        print('Wrong input argument, need send or receive')
        sys.exit()

    # socket connection info of server
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    clientSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    if send:
        # read the file: if send mode, add "0" at the beginning
        # if receive add "1" at the beginning of the string
        with open(file,'r') as f:
            sentence = f.read()
        sentence='0'+sentence
        clientSocket.send(sentence.encode('ascii'))
    else:
        sentence="1"
        sentence.encode('ascii')
        clientSocket.send(sentence.encode('ascii'))
        # receive data from server and print out
        modifiedSentence = clientSocket.recv(4096)
        modifiedSentence=modifiedSentence.decode("ascii")
        print(modifiedSentence)
        print('From Server: {}'.format(modifiedSentence))
    clientSocket.close()


