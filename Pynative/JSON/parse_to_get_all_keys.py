import json

"""
Practice Problem: https://pynative.com/python-json-exercise/#h-exercise-1-convert-the-following-dictionary-into-json-format
Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
"""

f = open("JSON_parse_to_get_all_keys.json")

data = json.load(f)

names = []
for data in data:
    names.append(data["name"])

print (names)