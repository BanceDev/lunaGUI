def server_packet():
    print("hello client")


def client_packet(packet_id, battery_volts):
    packet = f"{packet_id}\n"
    packet += f"BV:{battery_volts}"
    return packet