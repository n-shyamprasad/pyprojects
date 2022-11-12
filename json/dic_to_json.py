'''
Convert the following dictionary into JSON format
Input:
data = {"key1" : "value1", "key2" : "value2"}
Output:
data = {"key1" : "value1", "key2" : "value2"}
'''

import json

data = {"key1" : "value1", "key2" : "value2"}
jsondata = json.dumps(data)
print(jsondata)


#Access the value of key2 from the following JSON
samplejson = """{"color": "red", "type": "circle"}"""
dicdata = json.loads(samplejson)
print(dicdata['type'])

#pretty print json
jsond = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
prettyjson = json.dumps(jsond, indent=2, separators=(","," = "))
print(prettyjson)