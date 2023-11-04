import logging

#
# Creates a packet for the server (driver station) to send to client (robot)
#
# :param packet_id: id number of current packet
# :param joystick_let: a three item list that has the values for LSV, LSH, and LSP
# :param enable: a boolean for the current enable status of the robot
# :param operation_mode: an integer for current operation mode 0 = teleop, 1 = auto
# :returns: the compiled packet string for the server to send
#

def server_packet(joystick_left:list=None, enable:bool=None, operation_mode:int=None):
    packet = ""
    if not joystick_left == None:
        try:
            packet += f"LSV:{joystick_left[0]}\n"
            packet += f"LSH:{joystick_left[1]}\n"
            packet += f"LSP:{joystick_left[2]}\n"
        except IndexError:
            logging.error('Joysticks must be a list of length 3')
    if not enable == None:
        packet += f"EN:{enable}\n"
    if not operation_mode == None:
        packet += f"OP:{operation_mode}\n"
        
    return packet


#
# Creates a packet for the client based on what data the client passes
#
# :param packet_id: id number of current packet
# :param battery_volts: voltage for the battery on the robot
# :returns: the compiled packet string for the client to send
#

def client_packet(battery_volts:float):
    packet = f"BV:{battery_volts}"
    return packet