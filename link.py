#! /usr/bin/python
from linkedin import linkedin
import json
import json
CONSUMER_KEY = '#'
CONSUMER_SECRET = '#'
USER_TOKEN = '#'
USER_SECRET = '#'
RETURN_URL = 'http://localhost:8000'  

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())
 
app = linkedin.LinkedInApplication(auth)
 

connections = app.get_connections()
 
linkedin_contacts = 'contacts.json'
 
f = open(linkedin_contacts, 'w')
f.write(json.dumps(connections, indent=1))
f.close()
from prettytable import PrettyTable
pt = PrettyTable(field_names=['Name', 'Location'])
pt.align = 'l'
[pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name']))
for c in connections['values']
if c.has_key('location')]
print pt
