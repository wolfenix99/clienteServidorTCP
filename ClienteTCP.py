import socket
import threading
msgFromClient       = "Hello UDP Server"
serverAddressPort   = ("127.0.0.1", 20004)
bufferSize          = 1024
UDPClientSocket = socket.socket()
UDPClientSocket.connect(serverAddressPort);
c=4
c2=3
def request():
    global c
    while True:
        if c==0:
            print ("escuchando al servidor")
            mr=UDPClientSocket.recv(1024)
            ms2=mr.decode("utf-8")
            print (ms2)
            c=4
        if bytesToSend=="quit":
            break   


def main():
    h = threading.Thread(target=request)
    global c
    global c2
    global bytesToSend
   
    while True:
        if c>0: 
            print("porfavor ingrese el dato a enviar ")
            bytesToSend= input("-> ")
            ms=str.encode(bytesToSend)
            UDPClientSocket.sendto(ms,serverAddressPort)
            c=0
          
        if c2>0 and c==0:
            h.start()
            c2=0

        if bytesToSend =="quit":
            break
    
            


if __name__ == '__main__':
    main()