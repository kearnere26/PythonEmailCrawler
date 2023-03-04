import requests
import re

data = requests.get('https://www.uta.edu/academics/schools-colleges/business/undergraduate-advising/cob-advising')

emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data.text))

email_list = list(emails)

if len(emails) == 0:
    print('No Email address found.')
    print('--------------------------')
else:
    count = 1
    for item in emails:
        print('Email address #'+ str(count) + ': ' + item)
        count += 1












