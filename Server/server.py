#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
from queue import Queue

def run_server(out_q):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")


    while True:
        #  Wait for next request from client
        message = socket.recv_string()
        out_q.put(message)

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send(b"World")