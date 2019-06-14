#!/usr/local/bin/python3

from requests import get
from bs4 import BeautifulSoup

url = "https://www.49ers.com/team/players-roster/"

response = get(url)

print(response.status_code)

#print(response.content)

nfl = BeautifulSoup(response.content, 'html.parser')

#print(nfl.prettify())


#print(nfl.a)
#print(nfl.p)
nfl_body = nfl.body

#print(nfl_body.a)
#retrieves college from 49ers.com
print(nfl_body.div.main.contents[1].next_sibling.next_sibling.next_sibling.next_sibling.div.div.div.div.table.tbody.tr.contents[15])


