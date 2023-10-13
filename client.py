import socket

DISCONNECT = "Disconnect"
HEADER = 64
PORT = 5050

SERVER = '192.168.0.146'
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode('utf-8')
    msg_lenght = len(message)
    send_length = str(msg_lenght).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)




mes = True
while mes:
   message = input("[MESSAGE] ")
   send(message)
   if message == DISCONNECT:
     mes = False
