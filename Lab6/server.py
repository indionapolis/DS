import socket
import os
import sys
from threading import Thread

PORT = 5000


class ClientListener(Thread):

    def __init__(self, name: str, sock: socket.socket):
        super().__init__(daemon=True)
        self.sock = sock
        self.name = name

    def run(self):
        # null char for data separation
        data = self.sock.recv(1024).decode().split('\0')
        filename_original = data[0]
        filename = filename_original

        print(os.listdir('.'))
        # check uniqueness of the file name
        counter = 0
        while True:
            if os.path.exists(filename):
                filename = f'{filename_original.split(".")[0]}_copy{counter}.{ filename_original.split(".")[1]}'
                counter += 1
            else:
                break

        data = data[1].encode()

        # prepare new file
        with open(filename, 'wb') as f:
            f.write(data)
            # receive all data
            print('Ready for data data')
            while True:
                print('receiving data...')
                data = self.sock.recv(1024)
                if not data:
                    print('Got all data')
                    break
                # write data to a file
                f.write(data)

        f.close()

        self.sock.close()


def main():
    # set up server
    next_name = 1
    s = socket.socket()
    host = "localhost"
    s.bind((host, PORT))
    s.listen(5)

    print('Server listening ...')
    while True:
        # accept new connection and create handler in separate thread
        con, address = s.accept()

        print('connection from', address)

        name = 'u' + str(next_name)
        next_name += 1

        ClientListener(name, con).start()


if __name__ == '__main__':
    main()
