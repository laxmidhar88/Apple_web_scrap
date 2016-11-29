# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 04:40:12 2016

@author: Laxmidhar
"""
import urllib2
from lxml import html
from bs4 import BeautifulSoup
import HTMLParser
import json
link1=[]
listLink=[]
for i in range(2012,2015):
    initUrl='https://developer.apple.com/videos/wwdc'+str(i)+'/'
    html2 = urllib2.urlopen(initUrl).read()
    soup = BeautifulSoup(html2,'lxml')
    soup1=soup.find_all("section", class_="col-80 no-padding-top no-padding-bottom")
    for tag in soup1:
        lilnk = tag.a.get('href')
        link1.append(lilnk)
for i in range(2015,2017):
    initUrl='https://developer.apple.com/videos/wwdc'+str(i)+'/'
    html2 = urllib2.urlopen(initUrl).read()
    soup = BeautifulSoup(html2,'lxml')
    soup1=soup.find_all("section", class_="col-30 no-padding-top no-padding-bottom")
    for tag in soup1:
        lilnk = tag.a.get('href')
        link1.append(lilnk)
#i=0
for li in link1:
    #i+=1
    initUrll='https://developer.apple.com'+li
    urllist=initUrll.split('/')
    ssn=urllist[-2]
    yr=urllist[-3].replace("wwdc","")
    try:
        html2 = urllib2.urlopen(initUrll).read()    
        soup = BeautifulSoup(html2,'lxml')
        lilnk = soup.find('h1').getText()
        videoUrl=soup.find_all("li", class_="video")
        videoUrl=str(videoUrl)
        docUrl=soup.find_all("li", class_="document")
        docUrl=str(docUrl)
        vurl=BeautifulSoup(videoUrl,'lxml')
        durl=BeautifulSoup(docUrl,'lxml')
        vilnk = vurl.find_all('a')
        dlink = durl.find_all('a')
        if vilnk:
            hdv = vilnk[0].text
            hdvlnk = vilnk[0].attrs['href']
            if hdvlnk:
                hdvlnk= hdvlnk
            else: 
                hdvlnk=null
            sdv = vilnk[1].text
            sdvlnk = vilnk[1].attrs['href']
            if sdvlnk:
                sdvlnk=sdvlnk
            else :
                sdvlnk=null
        if dlink:
            pdfname = dlink[0].text
            pdf = dlink[0].attrs['href']
        else:
            pdf = null
        myjosondata={"tilte":lilnk,"year":yr,"sessionNumber":ssn,hdv:hdvlnk,sdv:sdvlnk,pdfname:pdf}
        listLink.append(myjosondata)
    except:
        pass
#    if i == 10:
#        break"""
lastjson={"sessions":listLink}
JsonData=json.dumps(lastjson,indent=4)
print JsonData
