import time
import zmq
from queue import Queue

#
# Creates a server context and socket using TCP.
# Then runs server and puts all incoming messages into a queue
#
# :param out_q: the queue to put the incoming messages into
#
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