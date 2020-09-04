#!/bin/bash

./client.py localhost 5555 send Message1.txt &
./client.py localhost 5556 send Message2.txt &
./client.py localhost 5557 send Message3.txt

./client.py localhost 5555 receive &
./client.py localhost 5556 receive &
./client.py localhost 5557 receive