# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:4/19/2018-11:11 AM
from urllib.request import urlopen
from xml.etree.ElementTree import parse

if __name__ == "__main__":
    # Download the RSS feed and parse it
    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)
    # Extract and output tags of interest
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print(title)
        print(date)
        print(link)