def delete_keys(dropped_keys, dictionary):
    if not isinstance(dropped_keys, list):
        return("First argument should contain a list of keys")
    if not isinstance(dictionary, dict):
        return("Second argument should contain a dictionary")
    
    new_dictionary = {}
    for i in dictionary:
        if i not in dropped_keys:
            new_dictionary[i] = dictionary[i]

    return(new_dictionary)


professor = {"first_name": "Mohamed", "last_name": "Farag", "birth_year": 1990, "nationality": "Egyptian"}
print("Before deletion, 'professor' contains:")
print(professor)
print("")
print("Now we have:")
print(delete_keys(["last_name", "birth_year"], professor))
