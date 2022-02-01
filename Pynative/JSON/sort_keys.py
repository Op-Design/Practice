import json

"""
Practice Problem: https://pynative.com/python-json-exercise/#h-exercise-1-convert-the-following-dictionary-into-json-format
Exercise 4: Sort JSON keys in and write them into a file
sampleJson = "{"id" : 1, "name" : "value2", "age" : 29}"
"""

# 1. Load JSON as dictionary
sampleJson = """{"id" : 1, "name" : "value2", "age" : 29}"""
loaded_data = json.loads(sampleJson)
print (loaded_data)
# 2. Save dictionary keys to array
data_keys = list(loaded_data.keys())
####print (data_keys)
# 3. Sort Array
data_keys_sort = data_keys.sort()
#### print (data_keys)
# 4. Use sorted array's values to create a new sorted dictionary
sorted_dictionary = {}
for key in data_keys:
    sorted_dictionary[key] = loaded_data[key]
print (sorted_dictionary)



