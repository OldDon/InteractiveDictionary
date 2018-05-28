import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data(w)
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y/N: " % get_close_matches(w, data.keys())[0]
        if yn == "y":
            return data[get_close_matches(w, data.keys()))[0]]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translate(word))

