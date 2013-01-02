#! /usr/share/python2

#usage python2 pythondaemon.py scripttoberunasdaemon.py args
#make sure that the script doesn't ask for user inputs but for system argv

from os import fork, chdir, setsid, umask, system
from sys import exit, argv
import time


def main():
  while 1: #you can change the infinity loop to something else if needed
      try:
          system("python2 "+ argv[1]) #here I use python2 but you can change it
          time.sleep(60)              #you can change the sleeping time for the loop
      except:
          time.sleep(120)
          system("python2 "+ argv[1])

# Dual fork
if __name__ == "__main__":
    #first fork
    try:
        pid = fork()
        if pid > 0:
            exit(0)
    except OSError, e:
        exit(1)

    chdir("/") #change that to the dir where you want the script to be exec from
    setsid()
    umask(0)

    #second fork
    try:
        pid = fork()
        if pid > 0:
            exit(0)
    except OSError, e:
        exit(1)
    main()


