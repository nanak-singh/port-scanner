import socket
import os
import sys
import time
from queue import Queue
import threading

queue = Queue()
portslist = range(1, 1024)
threadslist = []
portsresult = []
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def error():
    print("Invalid Input!!  Quitting the Interface...")
    sys.exit(1)

def openports():
    print("\nThe Open Ports are --> ", portsresult)


def end():
    print("\n\n------ PORT SCAN SUCCESSFULLY COMPLETED ------")
    
    

def portscan():
    print("\n\n------ ACTIVATING PORT SCAN ------\n")
    

try:
    prompt = int(input("\nChoose the Method of Input  ( 1: Enter the website || 2: Enter the IP adress ) --> "))
    if prompt > 2:
        print("INVALID ENTRY! ")
        sys.exit(1)
except:
    error()
    
if prompt == int(1):
    try:
        host = input("\nEnter the Website --> ")
        print("\n\n------ CHECKING YOUR INPUT ------")
        time.sleep(2)
        ip = socket.gethostbyname(host)
        print("\nYour Input is Valid! The IP Adress of {} is : {} ----> Additional info :)".format(host, ip))
        time.sleep(1)
        print("Redirecting to the Interface...")
    except:
        error()

if prompt == int(2):
        ip = input("\nEnter the IP Adress --> ")
        print("\n\n------ CHECKING YOUR INPUT ------")
        time.sleep(2)
        checkresult = os.system('ping -n 4 {}'.format(ip))
        if checkresult == 0:
            print("\nYour Input is Valid! Redirecting to the Interface...")
            time.sleep(3)
        else:
            error()
        
try:
    method = int(input("\nEnter the Scanning Method //>  1: MANUAL SCAN  2: AUTOMATIC SCAN --> "))
    if method >2:
        error()
except:
    error()

if method == 1:
    try:
        port = int(input("Enter the Port --> ")) 
    except:
        error()
    try:
        portscan()
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if a.connect((ip,port)) !=0:
            print("Port {} Status is: OPEN".format(port))
    except:
        print("Port {} Status is: CLOSED".format(port))
    end()
    time.sleep(5)
    sys.exit(0)

if method == 2:
    portscan()
    print("##### Detecting all OPEN ports... #####\n")
    def scan(port):
        try:
            a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.connect((ip,port))
            return True
        except:
            return False

    def insertqueue(portslist):
        for i in portslist:
            queue.put(i)

    def worker():
        while not queue.empty():
            port = queue.get()
            if scan(port):
                print("port {}  Status is: OPEN ".format(port) )
                portsresult.append(port)

    insertqueue(portslist)

    for j in range(800):
        threads = threading.Thread(target = worker)
        threadslist.append(threads)

    for threads in threadslist:
        threads.start()

    for threads in threadslist:
        threads.join()

    end()
    openports()
    time.sleep(15)
    sys.exit(0)
