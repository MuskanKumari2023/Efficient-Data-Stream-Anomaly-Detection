# SERVER
import socket
import pandas as pd
from utils import *

HOST = ''
PORT = 5051
data = add_trend() + add_pattern() + add_white_noise() + event()

data_points_iterator = iter(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("socket successfully created")
    s.bind((HOST, PORT))
    print("socket bind to %s" % (PORT))

    s.listen(2)
    print("socket is listening")
    
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            try:
                # Get the next data point from the DataFrame
                data_point = next(data_points_iterator)
                # Convert the data point to bytes and send it to the client
                conn.sendall(str(data_point).encode('utf-8'))
                
                # Receive the response from the client
                client_response = conn.recv(1024).decode('utf-8')
                print('Client response:', client_response)
                
            except StopIteration:
                print('All data points sent. Closing connection.')
                break