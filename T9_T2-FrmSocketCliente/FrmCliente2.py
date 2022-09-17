from socket import*
from tkinter import*
from threading import*

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "localhost"
portNumber = 26000

clientSocket.connect((hostIp, portNumber))

appcliente = Tk()
appcliente.title("Ventana cliente 2")
appcliente.config(bg="#CC9966")

lblTitulo = Label(text="Aplicación del Cliente 02", font=("Arial", 14), bg="#CC9966")
lblTitulo.grid(row=0, column=1, padx=50, pady=10)

txtMensajes = Text(appcliente, width=50)
txtMensajes.grid(row=1, column=1, padx=10, pady=10)

lblMensaje = Label(text="Mensaje: ", font=("Candara", 12), bg="#CC9966").place(x=10, y=460)

txtTuMensaje = Entry(appcliente, width=45)
txtTuMensaje.insert(0," ",)
txtTuMensaje.grid(row=2, column=1, padx=10, pady=10)

def enviarMensage():
    clientMessage = txtTuMensaje.get()
    txtMensajes.insert(END, "\n" + "Cliente 2: " + clientMessage)
    clientSocket.send(clientMessage.encode("utf-8"))
    txtTuMensaje.delete(0, "end")

btnSendMessage = Button(appcliente, text="Enviar", width=20, command=enviarMensage)
btnSendMessage.grid(row=3, column=1, padx=10, pady=10)

def recibirMensage():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        txtMensajes.insert(END, "\n" + "Cliente 1: " + serverMessage)

recvThread = Thread(target=recibirMensage)
recvThread.daemon = True
recvThread.start()

appcliente.mainloop()