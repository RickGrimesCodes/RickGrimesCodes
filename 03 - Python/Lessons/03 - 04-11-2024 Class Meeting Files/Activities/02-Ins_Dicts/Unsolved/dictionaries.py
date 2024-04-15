# we have used lists, that store data like....
"""
    subjects = ["Excel", "VBA", "Python"]
"""

# we can also use dictionaries which store data in key/value pairs like...

"""
city = {
"name": "Charlotte",
"state": "North Carolina",
"proTeams": ["Panters", "Hornets"]
}
"""

# to build this dictionary from scratch 
city = {} # uses the curly braces with no keys, denoting a list

# or 
city = dict() # uses the built in dict() function

# adding a single propery / key named "name" with a value
city = {"name": "Charlotte"}
print(f"{city['name']}") # use the square brackets wit hthe name to access the propery

# to update the value of a property
