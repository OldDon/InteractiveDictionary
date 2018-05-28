import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower() # .lower() makes characters in 'w' lowercase
    if w in data:        
        return data[w] # ORIGINAL return data(w) round brackets gives expectation of NOT dictionary
    elif len (get_close_matches(w, data.keys())) > 0: # checks there is something in the list
            yn = input("Did you mean %s instead? Enter y if yes, n if no" % get_close_matches(w, data.keys())[0] # prints out only the most similar word
            if yn == "y":
                return data[get_close_matches(w, data.keys())[0]]
    else:
        return "This term doesn't exist. Please check and re enter."

word = input("Enter word: ")

print(translate(word)) 


