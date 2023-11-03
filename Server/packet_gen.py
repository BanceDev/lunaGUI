def server_packet():
    print("hello client")


#
# Creates a packet for the client based on what data the client passes
#
# :param packet_id: the queue to put the incoming messages into
# :param battery_volts: voltage for the battery on the robot
# :returns: the compiled packet string for the client to send
#

def client_packet(packet_id, battery_volts):
    packet = f"{packet_id}\n"
    packet += f"BV:{battery_volts}"
    return packet