# python simple_markup.py > test_output.html
# convert simple text into html document

import re
from util import *

file = open('test_input.txt')

print('<html><head></head><body>')

title = True
for block in blocks(file):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')
