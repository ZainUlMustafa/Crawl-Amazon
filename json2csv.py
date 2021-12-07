import json
from pandas.io.json import json_normalize

with open('filepath.json') as dataFile:    
    data = json.load(dataFile) 

df = json_normalize(data)
df = df.drop("py/object", axis='columns')
df.to_csv("filepath.csv", index=False, sep=',', encoding="utf-8") #write to csv file
