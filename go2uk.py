#!/usr/bin/python3
import sys
import requests
import lxml.html as lh
import pandas as pd
from termcolor import colored
cmap = {}
def populate():
    url='https://www.gov.uk/guidance/red-amber-and-green-list-rules-for-entering-england'
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tables = doc.xpath('//table')
    for table in tables:
        color = None
        for t in table:
            if t.tag == 'thead':
                color = t.text_content().split()[0].lower()
                cmap[color] = []
            else:
                countries = [name for name in t.text_content().split('\n') if len(name.strip()) > 1 and not name.strip().startswith('Moved')]
                for c in countries:
                    key = c.strip().split()[0].lower()
                    cmap[key] = color
                    cmap[color].append(c.strip())
    
if len(sys.argv) > 1:
    populate()
    name = sys.argv[1].strip().lower()
    if name in ['red', 'amber', 'green']:
        color = 'yellow' if name == 'amber' else name
        for c in cmap[name]:
            print(colored(c, color))
    elif name in cmap:
        color = cmap[name]
        print(f'{sys.argv[1].capitalize()}: {colored(color, "yellow" if color == "amber" else color)}')
    else:
        print(f'Couldn\'t find country {colored(name.capitalize(), "blue")}')
