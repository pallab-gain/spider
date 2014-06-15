__author__ = 'xerxes'

from urllib2 import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import os
import subprocess as process
import re
base_url = "http://172.16.50.4/UPLOAD/6TB_1/ENGLISH%20TV%20Series/24%20%28TV%20Series%202001%E2%80%932010%29/"
pat = re.compile(r"(.*)(Season-[0-9])")
pat2 = re.compile(r"(.*)((.mp4)|(.mkv)|(.avi))")
def make_soup(url):
        html = urlopen(url).read()
        return BeautifulSoup(html, "lxml")

def get_links(url):
	links = make_soup(url).find_all('a',href=True)
	return links

class AnimeSpider():
    links = get_links(base_url)
    #print links
    for link in links:
        # if cur_link.endswith(".mp4"):
        #     cur_link = ''.join(["http://172.16.50.4/", cur_link])
        #     process.call(['axel', cur_link])
        cur_match = pat.match(str(link['href']))
        if cur_match:
        	cur_folder = cur_match.group(2)
        	sub_link = "%s%s"%("http://172.16.50.4",str(link['href']))
        	download_dir = "%s/%s"%(os.getcwd(),cur_folder)
        	os.mkdir(cur_folder)

        	_links = get_links(sub_link)
        	for _link in _links:
        		_cur_match = pat2.match( str(_link['href']) )
        		if _cur_match:
        			#print str(_link['href'])
        			download_link = "%s%s"%("http://172.16.50.4",str(_link['href']))
        			process.call(['axel',download_link], cwd=download_dir)

        	
        	

AnimeSpider()

