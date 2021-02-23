import json
import sys
from time import sleep
from tqdm import tqdm
import os

# python merge.py intents_new.json
tags=[]
patterns=[]
responses=[]


with open('intents_copy.json', 'r') as f:
    intents = json.load(f)


a=sys.argv[1]

with open(a, 'r') as f:
    intents1 = json.load(f)

for i in intents['intents']:
    tags.append(i['tag'])
    patterns.append(i['patterns'])
    responses.append(i['responses'])

for i in intents1['intents']:
    tags_x=i['tag']
    if tags_x in tags:
        x=tags.index(tags_x)
        y=intents['intents'][x]
        for j in i['patterns']:
            if j not in patterns[x]:
                y['patterns'].append(j)
        for k in i['responses']:
            if k not in responses[x]:
                y['responses'].append(k)
    else:
        dict1={'tag': i['tag'],
               'patterns': i['patterns'],
               'responses': i['responses'],
        }
        intents['intents'].append(dict1)
          

for i in tqdm(range(len(intents['intents']))):
    sleep(1)

with open('intents.json', 'w') as outfile:
    json.dump(intents, outfile,ensure_ascii=False, indent=4)

# os.remove(a)
# print("File Removed")
