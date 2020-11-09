------------------------ change user agent ---------------------------
import re
from requests_html import HTMLSession
import random

randomint = random.randint(0,7)
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
]
hdr = { 'User-Agent' : user_agents[randomint] }

or 
# to select from file
lines = open("user_agents.txt").read().splitlines()
user_agent =  random.choice(lines)
hdr = {"User-Agent": user_agent }


url = input("Enter URL: ")
session = HTMLSession()
# Use the object above to connect to needed webpage
resp = session.get(url, timeout=4, headers=hdr)

###########################################################################################################################
----------------------- request lib or js beautifier/ javascript beautifier----------------------
import beautify 
import requests

url = input("Enter URL: ")
response = requests.get(url,headers=headers)
soup = str(bs(response.text, "html.parser"))
print(beautify.js_beautify(soup))

for i in soup.head.contents:
    print(i)
for i in soup.find_all('script'):
    print (i.get('src'))

###########################################################################################################################
----------------------- request_html lib to load dynamic web content ----------------------
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from urllib.parse import urljoin


def get_session():
    url = input("Enter URL: ")
    session = HTMLSession()
    
    resp = session.get(url, timeout=4, proxies=proxies) #these parametrs can be removed if proxies not required 
     
    resp.html.render()

    soup = bs(resp.html.html, "lxml")
    print(soup.prettify())
    return soup

for i in soup.head.contents:
	print(i)
for i in soup.find_all('script'):
	print (i.get('src'))

script_files = []

    if script.attrs.get("src"):
        # if the tag has the attribute 'src'
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)
    if script.attrs.get("href"):
        # if the tag has the attribute 'href'
        script_url = urljoin(url, script.attrs.get("href"))
        script_files.append(script_url)

OR 

import requests
from bs4 import BeautifulSoup as bs

url = '<a href="http://some-domain.com/set/cookies/headers">http://some-domain.com/set/cookies/headers</a>'
 
headers = {'user-agent': 'your-own-user-agent/0.0.1'}
cookies = {'visit-month': 'February'}
 
req = requests.get(url, headers=headers, cookies=cookies)


###########################################################################################################################
---------------------- urllib ---------------------
import re
import urllib
response = urllib.request.urlopen(url)
html = response.read()
text = html.decode()
links = re.findall('"((http|ftp)s?://.*?).js"', text)
for link in links:
	print(link)


###########################################################################################################################
------------------------ file write utf-8 with codecs -----------------
import codecs
#import io
folder = input("Enter Folder name: ")
with codecs.open(folder+"/external_js_links.txt", "w","utf-8") as f:
	    for js_link in script_files:
	        print(js_link, file=f)
	return len(script_files)

###########################################################################################################################
------------------------------ file write utf-8 error ------------------------------

import codecs
#import io
folder = input("Enter Folder name: ")
with codecs.open(folder+"/external_js_links.txt", "w",encoding= 'unicode_escape') as f:
    for js_link in script_files:
        print(js_link, file=f)
    return len(script_files)
###########################################################################################################################
----------------------------- file read / open  ------------------------------------

with codecs.open(folder+"/external_js_links.txt", "r", "utf-8") as f:
    js_links = f.readlines()

js_links = [link.strip('\n') for link in js_links]

###########################################################################################################################
------------------------- File Unique lines/ remove duplicate lines ------------------------

uniqlines = set(open('/tmp/foo').readlines())

###########################################################################################################################
------------------------- Create directory if not found ------------------------
import os
folder = input("Enter Folder name: ")

if not os.path.exists(folder):
    os.mkdir(folder)

###########################################################################################################################
------------------------ Convert LIST to string ------------------------
STRING = "".join(str(x) for x in LISTA)

or 

STRING  = ''.join(listA)

###########################################################################################################################
-------------------------Find all Substrings from string -------------------------


import re
string = "<html> <script> alert(11) </script> Helo Bye <script> alert(22) </script> TATA</html>"

scripts = "<script"


matches = re.finditer("<script", string)
open_scripts = [match.start() for match in matches]

matches = re.finditer("</script>", string)
closed_scripts = [match.start() for match in matches]


print(open_scripts)
print(closed_scripts)


###########################################################################################################################
------------------------- compare two list items -------------------------------
>>> a = [1, 2, 3, 4, 5]                                                                                                                                                 
>>> b = [11, 2, 3, 4, 5] 
[i for i, j in zip(a, b) if i != j] 
ans : 1
[j for i, j in zip(a, b) if i != j] 
ans : 11  

###########################################################################################################################
---------------------------------------- Use SET OPERATIONS for comparing two files via hash values ----------------------------------

previous_hash_list = [1 , 2 , 3 , 4, 5]
new_hash_list =      [1 , 5, 2 , 4, 7]


if (len(previous_hash_list) == len(new_hash_list)):
    k = [j for i, j in zip(previous_hash_list, new_hash_list) if i != j]
else:
    print("May be new file is introduced or previous file removed")
    k = list(set(new_hash_list) - set(previous_hash_list))

print(k)

changed_hash_index = []
for item in k:
    changed_hash_index.append(new_hash_list.index(item))

# print(k)
print (changed_hash_index)

###########################################################################################################################
-------------------------- print colored text ----------------------------
from colorama import init 
from termcolor import colored 
init()
print(colored('Hello, World!', 'green', 'on_red')) 

###########################################################################################################################
--------------------------- Display text in center  ---------------------------
import shutil
center_point = shutil.get_terminal_size().columns   #screen center point

print("HELLO".center(center_point))

###########################################################################################################################
--------------------------- GET FILE NAME FROM URL name ---------------------------
def get_filename(url):
    return url.rsplit('/', 1)[1]

###########################################################################################################################
--------------------------- esc key infinite loop interrupt ---------------------
import msvcrt

while 1:
    print 'Testing..'
    # body of the loop ...
    if msvcrt.kbhit():
    if ord(msvcrt.getch()) == 27:
        break


"""
Here the key used to exit the loop was <ESC>, chr(27).

You can use the following variation for special keys:

    if ord(msvcrt.getch()) == 0:
        if ord(msvcrt.getch()) == 59:    # <F1> key
            break

With the following, you can discover the codes for the special keys:
    if ord(msvcrt.getch()) == 0:
        print ord(msvcrt.getch())
        break
        
Use getche() if you want the key pressed be echoed."""

###########################################################################################################################
---------------------------- global and local variable --------------------------------

x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

###########################################################################################################################
-------------------------- Convert string to hash value ----------------------------
import hashlib
def toHash(soup):
    hash = hashlib.md5(soup.encode()).hexdigest()
    return hash


###########################################################################################################################
-------------------------- string replace ---------------------------------------

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

###########################################################################################################################
------------------------------ Create LOGS --------------------------------
def create_log(folder):
    # temp_url = url.rsplit('.')
    # temp_url = temp_url[len(temp_url) - 2]
    f = folder+ "/" +  "exception_logs.txt"
    log = open(f, "a")
    log.seek(0)
    return log

log = create_log(folder)
print("################", file=log)

###########################################################################################################################
------------------------- print handle exception -----------------------------------------
except Exception as e: print(e)

except Exception:
        traceback.print_exc()

import traceback
error = 1
while error == 1:
    try:
        # do something here 
        error = 0
    except Exception:
        traceback.print_exc()
        print("Something")

or 

import sys
class HandleException(): 
    def __init__(self,error_info):
        self.exception_type, self.exception_object, self.exception_traceback = error_info
        self.filename = self.exception_traceback.tb_frame.f_code.co_filename
        self.line_number = self.exception_traceback.tb_lineno   

    def create_log(self):
        f = "exception_logs.txt"
        log = open(f, "a+")
        log.seek(0)
        print(datetime.now(), file = log)
        print("#######################",file = log)
        print("File name: ", self.filename,file = log)
        print("Line number: ", self.line_number,file = log)
        print("Exception_object: ", self.exception_object,file = log)
        print("Exception type: ", self.exception_type,file = log)
        print("exception_traceback: ", self.exception_traceback,file = log)
        print("#######################\n",file = log)

try:
    raise NotImplementedError("Not implemented")
except Exception:
    errors = HandleException(sys.exc_info())
    errors.create_log()

###########################################################################################################################
------------------------- File input dialogue box -------------------------------
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
print("SELECT FIRST FILE");
file_path = filedialog.askopenfilename()
file1 = open(file_path, 'r')


###########################################################################################################################
------------------------------- Empty file contents / clear file data ----------------------------------

def empty_file(folder, file):
    if os.path.exists(folder+"/"+file):
        try:
            f = open(folder + "/" + file, "r+")  
            # absolute file positioning 
            f.seek(0)  
            # to erase all data  
            f.truncate()
        except:
            pass
    else:
        return 


###########################################################################################################################
------------------------------- Schedule jobs with threading ----------------------------------

import threading
import time
import schedule


def job():
    print("I'm running on thread %s" % threading.current_thread())

def do_this():
    print("Second function")

def do_this_also():
    print("THIRD function")

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


j = schedule.every(10).seconds.do(run_threaded, job)
i = schedule.every(1).seconds.do(run_threaded, do_this)
k = schedule.every(1).seconds.do(run_threaded, do_this_also)


while 1:
    schedule.run_pending()
    time.sleep(1)
    # schedule.cancel_job(i)
