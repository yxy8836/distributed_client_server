#!/bin/bash

python3 client.py localhost 5555 send Message1.txt
python3 client.py localhost 5555 send Message2.txt
python3 client.py localhost 5555 send Message3.txt

python3 client.py localhost 5555 receive
python3 client.py localhost 5555 receive 
python3 client.py localhost 5555 receive
