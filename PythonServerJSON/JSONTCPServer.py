from socket import *
import threading
import random
import json

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
    print(f"Json received: {message}")
    nonJson = json.loads(message)
    return nonJson

def requestCheck(incomingDict: dict, socket):
    if "command" not in incomingDict:
        msg = "Missing 'command' in incoming message"
        sendMsg(msg, socket)
        return
    incomingCommand = incomingDict["command"].lower()
    
    if incomingCommand == "bad input":
        msg = "Bad input on client end! Try again"
        sendMsg(msg, socket)
        return True
    if incomingCommand == "exit":
        print("Closing connection")
        msg = "Closing connection, bye-bye!"
        sendMsg(msg, socket)
        socket.close()
        return False
    if incomingCommand not in commands:
        msg = f"command {incomingCommand} does not exist on server"
        sendMsg(msg, socket)
        return
    if "num1" not in incomingDict:
        msg = "Missing 'num1' in incoming message"
        sendMsg(msg, socket)
        return
    if "num2" not in incomingDict:
        msg = "Missing 'num2' in incoming message"
        sendMsg(msg, socket)
        return

    commands[incomingCommand](incomingDict,socket)
    return True

def sendMsg(message, socket):
    socket.send((message+"\n").encode())
    return

def randomcase(incomingDict: dict,socket):
    num1 = int(incomingDict["num1"])
    num2 = int(incomingDict["num2"])
    msg = str(random.randrange(num1, num2))
    sendMsg(msg, socket)
    return

def addcase(incomingDict: dict, socket):
    num1 = int(incomingDict["num1"])
    num2 = int(incomingDict["num2"])
    msg = str(int(num1+num2))
    sendMsg(msg, socket)
    return

def subtractcase(incomingDict: dict,socket):
    num1 = int(incomingDict["num1"])
    num2 = int(incomingDict["num2"])
    msg = str(int(num1-num2))
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
        nonJson = receive(socket)
        if not requestCheck(nonJson, socket):
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