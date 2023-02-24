myDict = {
    "fast": "In a Quick Manner",
    "himanshu": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'himanshu': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the values of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "himanshu": "A Writer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("himanshu")) # Prints value associated with key "harry"
print(myDict["himanshu"]) # Prints value associated with key "harry"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("himanshu2")) # Returns None as himanshu2 is not present in the dictionary
print(myDict["himanshu2"]) # throws an error as himanshu2 is not present in the dictionary