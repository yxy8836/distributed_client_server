Design:
Socket programming is used in this assignment, client.py in /client will build
connection with server using TCP protocol and send requests to the server. Requests
can be in two modes: send or receive.
In send mode, client program open and read text from a file, preappend a character "0"
before the string and send it to server.
In receive mode, client program send a request with a string, "1" and then
receive a message from server and print it to screen

server.py in /server will handle the connection request from client program, each time
there is a request from a client, a new process will be created and handle the request.
If the client sends a message, server will push it into the queue. If the client receives a
message, server will pop a message out of the queue and send it to the client. The shared
data, queue, is managed by multiprocessing module in python, which is process and thread
safe.

Assumptions:
Server is persistent, message in file has less than 3000 characters

Compile:
No need to compile the python code

Run:
Client (run on local)
python3 client.py "hostname" "port number" "send/receive" "filename"
example: python3 client.py bb136-05.mines.edu 5555 send Message1.txt

Server (run on server or localhost)
python3 server.py "port number"
example: python3 server.py 5555
Need Ctrl-c to terminate the program

Three message files are in the /client folder, the bash file can be run by
bash multiclient.sh
to test a multiple client requests case

***
There is another server_test_multiports.py under /server
which can be used to test multiple ports:
On server: python3 server_test_multiports.py 5555 5556 5557
On client: bash multiclient_multiport.sh


