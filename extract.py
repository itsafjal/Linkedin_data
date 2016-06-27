#! /usr/bin/python
#import json
#f=open("/root/Desktop/linkedin/contacts.json", "r")
contact=[]
import json
import pandas as pd

path="/root/Desktop/linkedin/final.txt"
link_data=[]
link_file=open(path, "r")

for line in link_file:
	try:
		link=json.loads(line)
		print link
		link_data.append(link)

	except:
		continue
print link_data
links=pd.DataFrame()
links['firstName']=map(lambda  link: link['values']['firstName'], link_data)
for line in links['firstName']:
	print line
