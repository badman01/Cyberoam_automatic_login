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
import getpass

from login import main

def logout(username):
    url = 'http://172.16.68.6:8090/logout.xml'
    post_data = 'mode=193' + '&username=' + username 
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print 'Logged out ' + username


if __name__ == '__main__':
    fob = open('logout_file')
    lines = fob.readlines()
    for line in lines:
    	logout(line[:8])