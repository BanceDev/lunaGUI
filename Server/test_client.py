#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import packet_gen
from random import randrange


packet_id = 0
port = "5555"

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://localhost:{port}")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    packet = packet_gen.client_packet(packet_id, randrange(0, 12))
    packet_id += 1
    socket.send_string(packet)

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))