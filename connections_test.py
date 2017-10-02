

import socket
import time
import os

# https://wiki.wireshark.org/CaptureSetup/CapturePrivileges


host = '10.114.2.137'
port = 1982



def check(host,port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
        print "Success connecting to "
        print host + " on port: " + str(port)
    except:
        print "****** Cannot connect to ******"
        print host + " on port: " + str(port)
    #except socket.error, e:
        #print "Connection to %s on port %s failed: %s" % (address, port, e)
        #return False
    return

n = 0
for x in range(4):
    print "Try :" + str(n)
    check(host,port)
    time.sleep(5)
    n = n + 1
    


