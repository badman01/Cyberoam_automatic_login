import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML
import time
from sys import argv
from urllib2 import Request, urlopen
import random
import threading

def login_req(username, password):
    url = 'http://172.16.68.6:8090/httpclient.html'
    post_data = 'mode=191' + '&username=' + username + '&password=' + password
    try:
        req = urllib2.Request(url, post_data)
        response = urllib2.urlopen(req)
        xml_dom = XML.parseString(response.read())
        document = xml_dom.documentElement
        response = document.getElementsByTagName('message')[0].childNodes[0].nodeValue
        if 'successfully' in response:
            return True
    except:
        return False  



def login():
    login_flag = 0
    while(login_flag == 0):
        id_list = [] #Enter the filenames from IDS folder in strng form here
        x = random.randint(0,13)
        fob = open("IDS/"+id_list[x])
        lines = fob.readlines()

        for line1 in (lines):
            line = random.choice(lines)
            if login_req(line[:8], id_list[x]) == True:
                print line[:8] + " " + id_list[x] + " " + "Login Successful"
                login_flag = 1
                break

    file_name = 'logout_file'
    logout_file = open(file_name,'w')
    logout_file.write(line[:8]+"\n")

    return line


def loggedin(user):
    url = "http://172.16.68.6:8090/live?" + "mode=192&username=" + str(user)
    res = urlopen(url).read()
    if "<ack><![CDATA[ack]]></ack>" in str(res):
        return True
    else:
        return False


def main():
    main.x = 0
    userid = '0'
    while(1):
        if main.x==0:
            userid = login()
            main.x = 1
        else:
            p = loggedin(userid)
            if p:
                time.sleep(5)
            else:
                print "Logged out...... Logging in......"
                userid = login()


if __name__ == '__main__':
    t = threading.Thread(target= main)
    t.start()