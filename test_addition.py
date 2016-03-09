command = car.add_hex2('\x20','\x0F')
car.command_send(command,1)




def add_hex2(self,hex1, hex2):
    tupleX = struct.unpack('1B',x)
    tupleY = struct.unpack('1B',y)

    tmp = tupleX[0] + tupleY[0]
    command = struct.pack('1B',tmp)
    return command


def command_send(command,duration):
    self.socket.send(command)
    time.sleep(duration)
