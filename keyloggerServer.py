import socket

PORT = 10000
HOSTNAME = 'localhost'
# HOSTNAME = socket.gethostbyname(socket.gethostname())

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (HOSTNAME,
                  PORT)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        file = open(f'{client_address[0]}-{client_address[1]}.txt', 'w')

        # Receive the data in small chunks
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                file.write(data.decode())
            else:
                print('no data from', client_address)
                file.close()
                break

    finally:
        # Clean up the connection
        connection.close()

# Source: https://pymotw.com/3/socket/tcp.html
