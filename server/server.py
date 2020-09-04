#!/usr/bin/env python

import socket as sk
import multiprocessing as mp
import sys

#define a function to handle request from client
def handle_request(queue,connection):
    # receive data up to 4096 bytes, and decode by ascii
    message=connection.recv(4096)
    msg=message.decode("ascii")

    # if the client is sending messages, put message in the queue
    if msg[0]=='0':
        queue.put(msg[1:])
        print("put in message: {}".format(msg[1:]))

    # if the client is receiving messages
    elif msg[0]=='1':
        # if queue is empty, send error to client
        if queue.empty():
            msgout="Error: no messages"
            print("no messages in the queue")
        # if queue is not empty, pop out message
        else:
            msgout=queue.get()
            print("pop out message: {}".format(msgout))
        # send encoded message from server to client
        connection.sendall(msgout.encode('ascii'))
    return None


if __name__ == '__main__':
    try:
        # the queue managed by multiprocessing shared data
        queue=mp.Manager().Queue()

        # build a connection between client and server
        serverPort = int(sys.argv[1])
        serverSocket = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
        serverSocket.bind(('',serverPort))
        serverSocket.listen(1)
        print('The server is ready to receive')

        # continuously running server app
        while 1:
            # the main process responsible for all handshaking connection
            # each time there is a request, start a new process and update the queue
            # queue is managed by multiprocessing module, process safe
            connectionSocket, addr = serverSocket.accept()
            newprocess=mp.Process(target=handle_request,args=(queue,connectionSocket,))
            newprocess.daemon=True
            newprocess.start()

    # need Ctrl-c to exit the server program, then terminate all processes
    finally:
        print("server program exit")
        for process in mp.active_children():
            process.terminate()