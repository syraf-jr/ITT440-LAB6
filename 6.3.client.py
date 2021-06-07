import socket
import signal
import sys

c = socket.socket()
host = '192.168.56.101'
port = 8888

print('Waiting for connection')
try:
    c.connect((host, port))
except socket.error as e:
    print(str(e))

Response = c.recv(1024)
print(Response.decode("utf-8"))
while True:
    print("CHOOSE AN MATHEMATICAL FUNCTION :")
    print("Logarithmic        [L]")
    print("Square Root        [S]")
    print("Exponential        [E]")
    print("SIN                [I]")
    print("COS                [C]")
    print("TAN                [T]")
    print("Logarithmic Base 2 [2]")
    Input = input('\nEnter Function Code: ')

    if Input == 'L' or Input == 'S' or Input == 'E' or Input == 'I' or Input == 'C' or Input == 'T' or Input == '2':
        num = input("Enter any number: ")
        Input = Input + ":" + num
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

    elif Input == 'exit':
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

c.close()