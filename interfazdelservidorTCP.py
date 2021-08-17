#un modulo es objeto de Python con atributos con nombres arbitrarios, no es otra cosa mas que un archivo con .py
from tkinter import * #Carga módulo tk (widgets estándar)
from tkinter import messagebox as mb
import socket #importa el modulo socket
import threading#importa los modulos de threading
localIP     = "127.0.0.1" #define la direccion ip
localPort   = 20004 #define el puerto donde estara a la escucha
bufferSize  = 1024 #define el numero de bytes 
TCPServerSocket = socket.socket() 
TCPServerSocket.bind((localIP, localPort)) 
TCPServerSocket.listen(10)      
(conexion,address)= TCPServerSocket.accept()
print ("nueva conexion")
print (address)
class Aplicacion():
   
    def __init__(self):
        self.c=4
        self.c2=3
        self.h = threading.Thread(target=self.request)
        self.h.start()
        #---------------------------------------------
        self.raiz = Tk() 
        self.raiz.geometry('600x500') 
        self.raiz.title('servidor') 
        self.raiz.configure(bg="gray") 
        self.raiz.resizable(width=False, height=False)
        #-------------------------------------------------------------
        self.en =Entry(self.raiz,width=50)
        self.en.grid(row=3,column=2,) 
        #-------------------------------------------------------------      
        self.et1 =Label(self.raiz,bg="gray",width=71,height=2,text="Para cerrar todo presiona el boton  \"salir\"")
        self.et1.grid(row=0,column=0,columnspan=3,sticky=W+E)
        #-------------------------------------------------------------
        self.binfo =Button(self.raiz,bg="blue",bd=5,text='Enviar',width=4,height=1,command=self.conexion)                                
        self.binfo.grid(row=3,column=1,pady=4)
        #-------------------------------------------------------------
        self.bsalir = Button(self.raiz,bg="red",bd=5, text='Salir',width=4,height=1,command=self.salir)                             
        self.bsalir.grid(row=3,column=0,pady=4,padx=12)
        #---------------------------------------------------------
        self.tinfo = Text(self.raiz,width=1,height=20)
        self.tinfo.grid(row=1,column=0,columnspan=3,sticky=E+W)
        self.photo = PhotoImage(file='./usuario.png')
        self.photo2= PhotoImage(file='./server.png')
        #-------------------------------------------------
        self.raiz.mainloop()

    def salir(self):
        if self.c2==6:
            self.raiz.destroy()
        else:
            mb.showerror("Cuidado","La conexion esta activa \nespera a que usuario se haya desconectado")
    def request(self):

        while True:      
            if self.c==4:
                ms=conexion.recv(bufferSize)
                self.message=ms.decode("utf-8")
                if self.message!="":
                    self.tinfo.config(state = "normal")
                    self.tinfo.insert(END,'\n')
                    self.tinfo.image_create(END, image=self.photo)
                    self.tinfo.insert(INSERT,self.message)
                    self.tinfo.insert(END,'\n')
                    self.tinfo.config(state = "disable")
                else:
                    msalir="el usuario "+str(address[1])+" ha dejado la conexion"
                    print(msalir)
                    self.tinfo.config(state = "normal")
                    self.tinfo.insert(INSERT,"\n"+ msalir)
                    self.tinfo.config(state = "disable")
                    self.c2=6
                self.c=0
            if self.c2>5:
                break
        print("adios")
       
        
    def conexion(self):
        if self.c==0 and self.c2!=6:
            bytesToSend= self.en.get()
            ms2=str.encode(bytesToSend)
            conexion.sendto(ms2,address)
            self.tinfo.config(state = "normal")
            self.tinfo.image_create(END, image=self.photo2)
            self.tinfo.insert(INSERT,bytesToSend)
            self.tinfo.config(state = "disable")
            self.c=4
        
def main(): 
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()