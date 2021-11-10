'''
The website 5000best.com/websites contains a list of the most 5000 visited/popular domains. They only display 100 domains per view, unless you click the next button,
the domain changes from "http://5000best.com/websites/1" to "http://5000best.com/websites/05" upon viewing the other pages. This code iterates through all the 
available pages and scraps the domains and stores it all in a (already created) file called "open.txt". This was made wit the idea of creating a whitelist of domains.
'''

import requests
import lxml.html

num = 51 # There are 50 sub-directories for the website url;
lis = []
while num > 1:
	num -= 1
	html = requests.get(f'http://5000best.com/websites/{num}')
	doc = lxml.html.fromstring(html.content)
	reaction = doc.xpath('//a[@class="n"]/text()') # The website stores all the domain address in a table anchor link with the class of "n";
	lis.append(reaction)
# // #
# Make sure you have an empty file named 'open.txt' within the same directory of the python file;
with open('open.txt', "a") as o:
	o.write(str(lis))