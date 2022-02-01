import json

"""
Practice Problem: https://pynative.com/python-json-exercise/#h-exercise-1-convert-the-following-dictionary-into-json-format
Exercise 1: Convert the following dictionary into JSON format
data = {"key1" : "value1", "key2" : "value2"}
"""


print ("\n")
data = {"key1" : "value1", "key2" : "value2"}
print (data)
print ("\n")

data_json = json.dumps(data, indent=4)
print (data_json)