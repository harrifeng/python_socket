import socket

__author__ = 'hfeng'

def main():
    HOST = ''
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    print "Connected by", addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()

if __name__ == '__main__':
    main()

