import socket
import os
import sys


def main():
    # connect to the server
    s = socket.socket()
    host = sys.argv[2]
    port = int(sys.argv[3])
    s.connect((host, port))

    # send file name
    filename = sys.argv[1]
    s.send((filename + '\0').encode())

    # prepare file transfer
    f = open(filename, 'rb')
    actual_size = os.path.getsize(f.name)

    # send data to the server
    data = f.read(1024)
    print('Start file sending')
    while data:
        s.send(data)
        print('--->', f'{f.tell()/actual_size*100:.2f}', '% of data sent')
        data = f.read(1024)
    f.close()

    print('Done sending')
    s.close()


if __name__ == '__main__':
    main()
