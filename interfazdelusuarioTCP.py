#un modulo es objeto de Python con atributos con nombres arbitrarios, no es otra cosa mas que un archivo con .py
from tkinter import * #Carga módulo tk (widgets estándar)
from tkinter import messagebox as mb
import socket #importa el modulo socket
import threading#importa los modulos de threading
msgFromClient       = "Hello UDP Server"
serverAddressPort   = ("127.0.0.1", 20004)
bufferSize          = 1024
UDPClientSocket = socket.socket()
UDPClientSocket.connect(serverAddressPort);

class Aplicacion():
    
    def __init__(self):
        self.c=4
        self.c2=3
        self.h = threading.Thread(target=self.request)
        #----------------------------------------------------
        self.raiz = Tk() 
        self.raiz.geometry('500x400')
        self.raiz.title('usuario') 
        self.raiz.configure(bg="lime") 
        self.raiz.resizable(width=False, height=False)
        #-------------------------------------------------------------
        self.en =Entry(self.raiz,width=50)
        self.en.grid(row=3,column=2,)
        #-------------------------------------------------------------      
        self.et1 =Label(self.raiz,bg="orange",width=71,height=2,text="Puedes cerrar la conexion con el boton \"salir\" \n")
        self.et1.grid(row=0,column=0,columnspan=3,sticky=W+E)
        #-------------------------------------------------------------
        self.binfo =Button(self.raiz,bg="blue",bd=5,text='Enviar',width=4,height=1,command=self.conexion)                                
        self.binfo.grid(row=3,column=1,pady=4)
        #-------------------------------------------------------------
        self.bsalir = Button(self.raiz,bg="red", bd=5,text='Salir',width=4,height=1,command=self.salir)                            
        self.bsalir.grid(row=3,column=0,pady=4,padx=12)
        #---------------------------------------------------------
        self.tinfo = Text(self.raiz,width=1,height=20)
        self.tinfo.grid(row=1,column=0,columnspan=3,sticky=E+W)
        #-------------------------------------------------------
        self.photo = PhotoImage(file='./usuario.png')
        self.photo2= PhotoImage(file='./server.png')
        #--------------------------------------------------
        self.raiz.mainloop()
    def salir(self):
        if self.c==4:
            self.bytesToSend="quit"
            self.raiz.destroy()
            UDPClientSocket.close()
        else:
            mb.showerror("Cuidado","la conexion esta activa \nespera a que el servidor te responda")

    def request(self):
        while True:
            if self.c==0:
                mr=UDPClientSocket.recv(bufferSize)
                self.tinfo.image_create(END, image=self.photo2)
                ms2=mr.decode("utf-8")
                self.tinfo.config(state = "normal")
                self.tinfo.insert(INSERT,ms2)
                self.tinfo.config(state = "disable")
                self.c=4

            if self.bytesToSend=="quit":
                break 
       
        
    def conexion(self):
         if self.c>0:
                self.bytesToSend=self.en.get()
                ms=str.encode(self.bytesToSend)
                UDPClientSocket.sendto(ms,serverAddressPort)
                self.tinfo.config(state = "normal")
                self.tinfo.insert(INSERT,'\n')
                self.tinfo.image_create(END, image=self.photo)
                self.tinfo.insert(INSERT,ms)
                self.tinfo.insert(INSERT,'\n')
                self.tinfo.config(state = "disable")
                self.c=0
         if self.c2>0 and self.c==0:
                self.h.start()
                self.c2=0

        
def main(): #define el metodo principal 
    mi_app = Aplicacion()#instancia el objeto de la clase aplicacion 
    return 0

if __name__ == '__main__':
    main()
