import zmq
import packet_gen
from random import randrange


port = "5555"

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://localhost:{port}")

#  Do 10 requests, waiting each time for a response
for request in range(100):
    packet = packet_gen.client_packet(float(randrange(0, 12)))
    socket.send_string(packet)

    #  Get the reply.
    message = socket.recv_string()
    print("Received reply %s [ %s ]" % (request, message))