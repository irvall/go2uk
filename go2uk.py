#!/usr/bin/python3
import sys
import requests
import lxml.html as lh
from termcolor import colored
url = 'https://www.gov.uk/guidance/red-amber-and-green-list-rules-for-entering-england'
cmap = {}


def populate():
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    for tables in doc.xpath('//table'):
        colour = None
        for table in tables:
            if table.tag == 'thead':
                colour = table.text_content().split()[0].lower()
                cmap[colour] = []
            else:
                countries = [name for name in table.text_content().split('\n')
                             if len(name.strip()) > 1 and not name.strip().startswith('Moved')]
                for c in countries:
                    key = c.strip().split()[0].lower()
                    cmap[key] = colour
                    cmap[colour].append(c.strip())


def show_colour(*colours):
    delimit = '\n* '
    for colour in colours:
        cs = cmap[colour]
        text_colour = "yellow" if colour == "amber" else colour
        print(
            f'{colored(colour.capitalize(), text_colour)} ({len(cs)} countries):', end=delimit)
        print(delimit.join(cmap[colour]))
        print()


populate()
if len(sys.argv) > 1:
    arg = sys.argv[1].strip().lower()
    if arg in ['red', 'amber', 'green']:
        show_colour(arg)
    elif arg in cmap:
        colour = cmap[arg]
        print(
            f'{sys.argv[1].capitalize()}: {colored(colour, "yellow" if colour == "amber" else colour)}')
    else:
        print(f'Couldn\'t find country {colored(arg.capitalize(), "blue")}')
else:
    show_colour('red', 'amber', 'green')
