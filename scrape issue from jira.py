from jira import JIRA
import requests
import json


import pandas as pd
username = ''
password = ''
jira = JIRA(basic_auth=(username, password), options = {'server': ''})


projects = jira.projects()
keys = sorted([project.key for project in projects])[0:]
my_key=[]
for i in keys:
    if i=="RD":
        my_key.append(i)
fields=[]
k=0
for project in my_key:
    issues = jira.search_issues('project=RD', maxResults=None)
    for i in issues:
        if k<3:
            k=k+1
            fields.append(jira.issue(i).raw)
        else:
            break
print(fields)
