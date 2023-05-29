import difflib
import json
with open('data.json') as f:
    file = json.load(f)
#print(file)
word = input("Enter word to search ")
words = word.lower()
if words in file:
    print(words,':',file[words])
else:
    matches= difflib.get_close_matches(words,file.keys(),n=3,cutoff=0.6)
    if len(matches) > 0:
        # Prompt the user if they want to see the suggested words
        choice = input(f"Did you mean {matches[0]}? Enter Y for yes, N for no: ")
        if choice.upper() == "Y":
            print(file[matches[0]])
        else:
            print("Word not found.")
    else:
        print("Word not found.")