import socket
import ctypes

PATH = "./socket/"
HOST = '192.168.88.145'
PORT = 9000

# Main
def main ():
    # Initialize socket
    print ("Initializing socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)


    conn, addr = s.accept()
    with conn:
        print ("Connection initialized!")
        while True:
            income_data = conn.recv(1024)
            if income_data:
                print (income_data)
                libmain = ctypes.cdll.LoadLibrary("./libmain.so")
                libmain.function(income_data)
    print ("Exited")

if __name__ == '__main__':
    main()