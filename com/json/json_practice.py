'''
Created on May 17, 2018

@author: walchen
'''
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

json_object = json.loads(jsonData)
print json_object
print json_object["c"]
json_str = json.dump(jsonData)
print json_str
