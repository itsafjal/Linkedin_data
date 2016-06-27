#! /usr/bin/python
from linkedin import linkedin
import json
CONSUMER_KEY = '#'
CONSUMER_SECRET = '#'
USER_TOKEN = '#'
USER_SECRET = '#'
RETURN_URL = 'http://localhost:8000' 

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())
 
app = linkedin.LinkedInApplication(auth)
 

connections = app.get_companies(company_ids=[1035], universal_names=['apple'], selectors=['name'], params={'is-company-admin': 'true'})
 
linkedin_contacts = 'company_contacts.json'
 
f = open(linkedin_contacts, 'w')
f.write(json.dumps(connections, indent=1))
f.close()
from prettytable import PrettyTable
pt = PrettyTable(field_names=['id', 'Universal-Name'])
pt.align = 'l'
[pt.add_row((c['id'] + c['universl-name']))
for c in connections['values']
if c.has_key('id')]
print pt

