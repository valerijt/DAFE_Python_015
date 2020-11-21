import json

'''
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

'''

'''
Python                  JSON

dict                -> object
list, tuple         -> array
str                 -> string
int, long, float    -> number
True                -> true
False               -> false
None                -> null

'''

# dump() -> file
# dumps() -> string

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

#with open('data_file.json', "w") as write_file:
#    json.dump(data, write_file)

# my_data = json.dumps(data)

my_data = json.dumps(data, indent=4) # separators

print(my_data)