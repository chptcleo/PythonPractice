'''
Created on May 17, 2018

@author: walchen
'''
import json, os


def process_with_memory():
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    
    json_object = json.loads(jsonData)
    print(json_object)
    print(json_object["c"])
    json_str = json.dumps(json_object, ensure_ascii=False)
    print(json_str)

    
def process_with_file():
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    cur_dir = os.path.dirname(__file__)
    file_location = os.path.join(cur_dir, 'json_file')
    with open(file_location, 'wb') as f:
        json.loads(jsonData, f)


if __name__ == '__main__':
    process_with_memory()
    process_with_file()

