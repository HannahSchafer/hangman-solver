
import os
import requests
import json

# Logic for hangman.py:
# -integrate with dictionary API 
# -send to my client, then their server a letter, based on heuristics of most common letters in english language.
# - once i get my first letter in the word, start to compare to words from the dictionary, where that letter is in that position
# - get most common letters from those remaining words; throw them one by one at the game until my next hit, then repeat process. 
# -

def connect_oxford():
    """Connect with Oxford dictionary API."""

    app_id=os.environ["OXFORD_APP_ID"]
    app_key=os.environ["OXFORD_APP_KEY"]

    url = 'https://od-api.oxforddictionaries.com/api/v1/wordlist/en/lexicalCategory%3DNoun%2Cverb%2Cadjective%2Cadverb%3B?word_length=10'

    wordlist = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    print type(wordlist)
    print("text \n" + wordlist.text)
    return wordlist


print connect_oxford()