import json

with open('sample1.json', 'r') as f:
    intents = json.load(f)


dict1={}
dict2={}
list1 = []
pattern_list = []
responses_list = []
i=0
for key,value in intents.items():
    if key == 'conversations':
        for i in range((len(intents['conversations']))):
            pattern_list = []
            responses_list = []
            tag = str(str(intents['categories'][0])) +" "+str(i)
            patterns = (intents['conversations'][i][0])
            responses = (intents['conversations'][i][1])
            print(patterns,tag,responses,i)
            pattern_list.append(patterns)
            responses_list.append(responses)
            dict2 = {"tag":tag,"patterns":pattern_list,"responses":responses_list}
            list1.append(dict2)
            print(list1)
    if key == 'categories':
        #print(key)
        key = str(intents['categories'][0])
        
        dict1.__setitem__(str(key),list1)
        #print("%%%%%%"+ str(key))

print(intents.keys())

with open('sample_output.json', 'w') as outfile:
    json.dump(dict1, outfile,ensure_ascii=False, indent=2)