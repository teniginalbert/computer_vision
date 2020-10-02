#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:15:44 2020

@author: alberttenigin
"""

import socket

HOST = ''
PORT = 9002

s = socket.socket()
s.bind((HOST, PORT))

s.listen(1)

while(True):
    clientSocket, clientAddress = s.accept()   
    stop = ''
    # Handle one request from client
    while(stop != 'stop'):
        data = clientSocket.recv(1024)
        data = data.decode()
        print("At Server: %s"%data)

        if(data!=b''):
            # Send back what you received
            stop = data
            clientSocket.send(data.upper().encode())
            break
        
    clientSocket.close()