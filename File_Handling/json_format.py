'''
Working with JSON files

Javascript Object Notation

Similar to python dictionary


Here there are two things need to be done while using json

Serialization -> Python object to JSON String (Write operation)
Deserialization -> Converting JSON String to Python Object (Read operation)
'''
import json

# Reading Json file
with open('todos.json','r') as file:
    # Deserialisation of json
    data = json.load(file)
    print(data)

#  string to object means use loads()
# If it is already a json object use load
# The json. load() is used to read the JSON document
#  from file and The json. loads() is used to convert 
# the JSON String document into the Python dictionary.



# Writing to json file
marks_dict = {
    "students":[ 
        {
        "roll_no":12,
        "name":"abc",
        "marks":99
        },
         {
            "roll_no":9,
            "name":"abc",
            "marks":99
        }
    ]
}

with open("marks.json",'w') as file:
    # To dump with json indent use indent parameter
    # And there are many more we can also sort based on keys
    # using sort_keys as True
    json.dump(marks_dict,file, indent=True, sort_keys=True)
    
    # To convert pytjon object to json formatted string
    json_str = json.dumps(marks_dict, indent=True, sort_keys=True)
    print(type(json_str),json_str)
    

