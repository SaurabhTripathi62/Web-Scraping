# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:40:18 2018

@author: saurabh tripathi HP
"""

import requests
import lxml.html

url='https://gaana.com/artist/sia'
path='.//div[@class="playlist_thumb_det"]/a'+'/text()'
print(path)
response=requests.get(url)
bytecode=lxml.html.fromstring(response.content)
source=bytecode.xpath(path)
print('source: ',source)

'''
output:
    .//div[@class="playlist_thumb_det"]/a/text()
source:  ['Cheap Thrills', 'Thunderclouds', 'Limitless from the Movie "Second Act"',
'Dusk Till Dawn (Radio Edit)', "I'm Still Here", 'Genius', 'Titanium (feat. Sia) [Extended]'
, 'Cheap Thrills', 'Chandelier', 'Mountains', 'Bang My Head (feat. Sia & Fetty Wap)', 'Flames',
'Audio', 'The Greatest', 'Crying in the Club', 'Never Give Up', 'Cheap Thrills', 'Cheap Thrills', 
'Chained To The Rhythm', 'Unstoppable', 'We Are One (Ole Ola) (The Official 2014 Fifa World Cup Song)'
, 'Move Your Body (Single Mix)', 'Salted Wound(From The', 'Helium', 'Elastic Heart', 'Alive', 'Beautiful Pain'
, 'Cheap Thrills (Hex Cougar Remix)', 'Titanium', 'Helium (Sia vs. David Guetta & Afrojack)', 
'Titanium (feat. Sia) [Alesso Remix]', 'The Greatest', 'Dusk Till Dawn (Brooks Remix)',
'We Are One (Ole Ola) [The Official 2014 FIFA World Cup Song]', 'Move Your Body', 'Waterfall', 
'Chandelier', 'House On Fire', 'Guts Over Fear', 'Bird Set Free']
'''
