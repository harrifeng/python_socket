__author__ = 'hfeng'
import socket

def main():
    HOST = "127.0.0.1"
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    sin = raw_input("->")
    s.sendall(sin)
    data = s.recv(1024)
    s.close()
    print "Received", repr(data)

if __name__ == "__main__":
    main()
