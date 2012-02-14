"""
scrape.py
Screen-scraping demo: open a page, find and print the first anchor element
modified for assignment: File Downloader
"""

import urllib2
from pprint import pprint
from BeautifulSoup import BeautifulSoup
import os
import sys

def download_from_url(url, extension):
    page = urllib2.urlopen(url).read()  # now page is one big string

    soup = BeautifulSoup(page)
    fullpath=[]
    # find all the anchor tags that link to Python files
    pythonfiles = soup.findAll('a',attrs={'href':(lambda a: a and a.endswith(extension))})

    for nfile in pythonfiles:
        link= nfile['href']
        fullpath.append(link)


    for n, fileNow in enumerate(fullpath):
        remote_url="%s/%s" %(url,fileNow)
        remoteFile=urllib2.urlopen("%s/%s" %(url,fileNow))
        localFile=open(remote_url.split('/')[-1],'w')
        localFile.write(remoteFile.read())
        localFile.close()
        

if __name__ == '__main__':
    url = "http://jon-jacky.github.com/uw_python/winter_2012/" # course page
    extension=".py" # ".txt"
    download_from_url(url, extension)
