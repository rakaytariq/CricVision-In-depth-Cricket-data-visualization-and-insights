from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import re 

def getTestRanks(url):
    link = url
    html_page = request.urlopen(link);
    soup = BeautifulSoup(html_page,'lxml')
    table = soup.find_all('table',class_="StoryengineTable")
    data = table[0].get_text()
    #Rough cleaning to store as an excel file
    clean_data = re.sub('(\\n)',',',data)
    clean_data = re.sub('(,,,,|,,,|,,)',' \n ',clean_data)
    clean_data = re.sub(',',' \t ',clean_data)
    with open('TestRanks.xslx','w') as f:
        f.write(clean_data)
    print("Successfully got the data.")

url = "http://www.espncricinfo.com/rankings/content/page/211271.html"
getTestRanks(url)
