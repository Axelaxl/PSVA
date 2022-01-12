#!/usr/bin/env python
# Author : Axel axl
import sys
import socket
import subprocess
from datetime import datetime

subprocess.call('clear', shell=True)


def closePort(ip, posts):
    start = datetime.now()
    scan_date = str(start).split()[0]
    start_time  = str(start).split()[1].split('.')[0]

    remoteServerIP = socket.gethostbyname(ip)
    print( "-" * 65)
    print( "    Please wait, close remote host post", remoteServerIP)
    print( "-" * 65)

    try:
        for port in range(1, posts):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("...".format(sock))
                sock.close()
                print(port + ' port has been close.')
            

            sock.close()

    except KeyboardInterrupt:
        print( "You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print( 'Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print( "Couldn't connect to server")
        sys.exit()

    end = datetime.now()
    end_time  = str(end).split()[1].split('.')[0]
    total_time = str(end - start).split('.')[0]

    print('\n')
    print( 'Scanning Started in: ', start_time)
    print( 'Scanning Completed in: ', end_time)


if __name__ == '__main__':
    ip = "192.168.122.165"
    #ip = "192.168.43.133"
    #remoteServer = input("Enter a remote host to scan: ")
    ports = 65000
    closePort(ip, ports)
