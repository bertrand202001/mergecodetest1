#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:36:46 2019

@author: yujzhang
"""
import re

s = """<div class="animal">
  <p class="name">
      <a title="Tiger"></a>
  </p>
  
  <p class="contents">
    Two tigers two tigers run fast
  </p>
</div>

<div class="animal">
  <p class="name">
      <a title="Rabbit"></a>
  </p>
  
  <p class="contents">
    Small white rabbit white and white
  </p>
</div>"""

p = re.compile('<div class="animal".*?title="(.*?)">.*?contents">(.*?)</p>',re.S)

r = p.findall(s)
print(r)

for animal in r:
    print("Animal Name:",animal[0].strip())
    print("Animal Description:",animal[1].strip())

