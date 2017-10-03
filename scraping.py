import pymongo
from lxml import html

import requests

import re
import time 

'''
timestamp = str(time.time())

filename = 'nytimes_data_' + timestamp + '.txt'

textfile = open(filename, 'w')
'''

def scrapeText(link):
    ##Retrieve the page using https get method
    
    page = requests.get(link)
    
    ## creates a tree structure
    
    tree = html.fromstring(page.content)
        
    
    ## Parse content out based on the three common tags and classes used by NYT html formatting standards
    
    content = tree.xpath('//div[@class="articleBody"]/text()')
    
    content = content + tree.xpath('//p[@class="story-body-text story-content"]/text()')
    
    content = content + tree.xpath('//p[@class="story-body-text"]/text()')
    
    
    ## Combine the list into a single string
    
    text = ''.join(content)

    return text
    
    '''
    ## writes to file...can change later.
    textfile.write(text)
    textfile.write('\n')
    '''
    
    
    
