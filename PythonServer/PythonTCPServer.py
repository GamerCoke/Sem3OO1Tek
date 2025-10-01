from socket import *
import threading
import random

#########
# Defining server 
serverport = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverport))
serverSocket.listen(5)
                                                                                                                                #
                                                                                                                        #########

#########
# Deffinitions & Functions
def receive(socket):
    message = socket.recv(1024).decode("latin-1").strip()
    print(f"Message received: {message}")
    return message

def requestCheck(message):
    return message.lower().split(" ", 1)

def numberHandling(message):
    return message.split()

def sendMsg(message, socket):
    socket.send((message+"\n").encode())
    return

def endcase(socket):
    print("Closing connection")
    msg = "Closing connection, bye-bye!"
    sendMsg(msg, socket)
    socket.close()

def randomcase(socket):
    print("Random command called")
    msg = "Input numbers"
    sendMsg(msg, socket)
    msg = receive(socket)
    numbers = numberHandling(msg)
    if (len(numbers)== 2):
        msg = str(random.randrange(int(numbers[0]), int(numbers[1])))
        sendMsg(msg, socket)
    elif (len(numbers)>2):
        msg = "Too many numbers, function only supports 2 input numbers"
        sendMsg(msg, socket)
    elif (len(numbers)<2):
        msg = "Too few numbers, function only suppoorts 2 input numbers"
        sendMsg(msg, socket)
    return

def addcase(socket):
    print("Add command called")
    msg = "Input numbers"
    sendMsg(msg, socket)
    msg = receive(socket)
    numbers = numberHandling(msg)
    if (len(numbers)== 2):
        msg = str(int(numbers[0])+int(numbers[1]))
        sendMsg(msg, socket)
    elif (len(numbers)>2):
        msg = "Too many numbers, function only supports 2 input numbers"
        sendMsg(msg, socket)
    elif (len(numbers)<2):
        msg = "Too few numbers, function only suppoorts 2 input numbers"
        sendMsg(msg, socket)
    return

def subtractcase(socket):
    print("Subtract command called")
    msg = "Input numbers"
    sendMsg(msg, socket)
    msg = receive(socket)
    numbers = numberHandling(msg)
    if (len(numbers)== 2):
        msg = str(int(numbers[0])-int(numbers[1]))
        sendMsg(msg, socket)
    elif (len(numbers)>2):
        msg = "Too many numbers, function only supports 2 input numbers"
        sendMsg(msg, socket)
    elif (len(numbers)<2):
        msg = "Too few numbers, function only suppoorts 2 input numbers"
        sendMsg(msg, socket)
    return
                                                                                                                                #
                                                                                                                        #########

#########
# Dictionaries
commands = {
    "random": randomcase,
    "add": addcase,
    "subtract": subtractcase
}

                                                                                                                                #
                                                                                                                        #########
           
#########
# Actual Server
def service(socket):
    while True:
        message = receive(socket)
        request = requestCheck(message)[0]
        if request in commands:
            commands[request](socket)
        if request=="exit":
            endcase(socket)
            break
                                                                                                                                #
                                                                                                                        #########
   
#########
# Initialisation of server
print(f"Server is ready to print")
welcomeMsg = "Connection established, Hello!"
while True:
    connectionSocket, address = serverSocket.accept()
    print(f"Connection established with {address}")
    sendMsg(welcomeMsg, connectionSocket)
    threading.Thread(target=service, args=(connectionSocket,)).start()
                                                                                                                                #
                                                                                                                        #########