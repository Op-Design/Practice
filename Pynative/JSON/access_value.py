import json

"""
Practice Problem: https://pynative.com/python-json-exercise/#h-exercise-1-convert-the-following-dictionary-into-json-format
Exercise 2: Access the value of key2 from the following JSON
sampleJson = {"key1": "value1", "key2": "value2"}
"""


print ("\n")
sampleJson = """{"key1": "value1", "key2": "value2"}"""
print (sampleJson)
print(type(sampleJson))
print ("\n")

sampleJson_loaded = json.loads(sampleJson)
print (sampleJson_loaded["key2"])
print(type(sampleJson_loaded))