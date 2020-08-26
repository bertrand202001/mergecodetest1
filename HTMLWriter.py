#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:45:00 2020

@author: yujzhang
"""

import pandas as pd

content = []

with open("./test") as fp:
   ct = fp.readlines()     

for x in ct:
    content.append(x.split(" "))

pdd = pd.DataFrame(content)
print(pdd)

html_string_start = '''
<html>
  <head><title>Existing Steps</title></head>
  <link rel="stylesheet" type="text/css" href="mystyle.css"/>
  <body>
'''
html_string_end = '''
  </body>
</html>
'''

with open(r'./result3.html', 'w') as f:
    f.write(html_string_start)
    f.write('<table>')
    for header in pdd.columns.values:
        f.write('<th>'+str(header)+'</th>')
    for i in range(len(pdd)):
        f.write('<tr>')
        for col in pdd.columns:
            value = pdd.iloc[i][col]    
            f.write('<td>'+str(value)+'</td>')
        f.write('</tr>')
    f.write('</table>')
    f.write(html_string_end)
