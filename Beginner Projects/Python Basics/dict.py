# Dictionaries in python are similar to JSONs in JS
# Uses {Key : Value} syntax
# Seperate values by commas

programming_dict = {"Bug": "NO!!",
                    "Function": "see this! makes sense!"}

# How Do I retrieve an item from a dictionary?, Well this is how you do it

print(programming_dict["Bug"])


# How do i add new items for a dicitonary?
programming_dict["Loop"] = 'The action of doiing dover sfomsodf'

print(programming_dict["Loop"])

# You can also create an empty dictionary like...
empty_dictionary = {}

# You can also wipe an exisiting dictionary by doing this
programming_dict = {}

L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[2][2])
# Prints ['eee', 'fff']

print(L[2][2][0])

# Get the value of the "model" key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:

# Example
# Get the value of the "model" key:

x = thisdict.get("model")

# You can also do .copy to copy

mydict = programming_dict.copy()

# Print all key names in the dictionary, one by one:

for x in thisdict:
    print(x)

# Create a dictionary that contain three dictionaries:

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
