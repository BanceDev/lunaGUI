import time
import zmq
import logging
import Server.packet_gen as srv_gen
from queue import Queue

#
# Creates a server context and socket using TCP.
# Then runs server and puts all incoming messages into a queue
#
# :param out_q: the queue to put the incoming messages into
# :param in_q: the queue to recieve outgoing messages from
#
def run_server(out_q:Queue, in_q:Queue):
    #logging setup and formatting
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler('server.log')
    f_handler.setLevel(logging.INFO)
    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.setLevel(logging.DEBUG)

    # start zmq socket of type PAIR
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    logger.info('Driver station socket started')


    while True:
        #  Wait for next request from client
        message = socket.recv_string()
        logger.info('Recieved robot packet')
        out_q.put(message)

        #  Do some 'work'
        time.sleep(1)

        if not in_q.empty():
            print("smth in queue")
            socket.send_string(in_q.get())
        else:
            socket.send_string(srv_gen.server_packet())