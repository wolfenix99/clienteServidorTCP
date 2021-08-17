#un modulo es objeto de Python con atributos con nombres arbitrarios, no es otra cosa mas que un archivo con .py
import socket
import threading
localIP     = "127.0.0.1" #define la direccion ip
localPort   = 20004 #define el puerto donde estara a la escucha
bufferSize  = 1024 #define el numero de bytes 
c=4 #inicia la variable de control con un numero diferente de cero
c2=5
TCPServerSocket = socket.socket() #define el puerto y la direccion ip donde se mantendra ala escucha
TCPServerSocket.bind((localIP, localPort)) #Tenemos ahora que indicar en qué puerto se va a mantener a la escucha 
#nuestro servidor utilizando el método bind. 
TCPServerSocket.listen(10)
print("TCP server up and listening")           
(conexion,address)= TCPServerSocket.accept()
print ("nueva conexion")

def request():
    global c
    while True:
        if c==0:
            print("porfavor ingrese el dato a enviar ")
            bytesToSend= input("-> ")
            ms2=str.encode(bytesToSend)
            conexion.sendto(ms2,address)
            c=4
        if message=="quit":
            break
        


def main():
    h = threading.Thread(target=request)
    global c
    global c2
    global address
    global message
    while True:

        if c>0:
            print (address)
            ms=conexion.recv(1024)
            message=ms.decode("utf-8")
            print(message)
            c=0
        if message== "quit":
            break 
        if c2>0 and c==0:
            h.start()
            c2=0
          
    print("adios")
    conexion.close() #cancela la 

if __name__ == "__main__":
    main()
