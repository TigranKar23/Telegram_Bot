import json
ar = []
with open('cenz.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

#json fil e, write,
with open('cenz.json','w', encoding='utf-8') as e: 
    #json-ում լցնելը
    json.dump(ar, e) 