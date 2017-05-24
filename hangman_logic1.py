# encoding=utf8  
from nltk.corpus import words
import re
import requests
import json



def make_word_buckets(word_list):
    """Sorts all English words into dictionary, where key is word length."""

    word_list = words.words()

    #236,736 words total
    # print len(word_list)

    word_length_dict = {}
    for word in word_list:
        if word[0].islower():
            word_length_dict.setdefault(len(word),[]).append(word)

    return word_length_dict

# print make_word_buckets(word_list)


def make_letter_frequencies(word):

    pass


def choose_bucket(word_length):
    """Picks bucket based on length of word. Refines bucket as more letters unveiled."""

    #we know word length by initial number of guesses left

    return 


# -sort all words into buckets based on length
# - get a frequency list per bucket - frequency of letters by bucket of length of word 
# - use regex to pattern match all words from list into smaller list. take new frequency letter list. 
# -repeat

def start_game():

    email = 'schafer.hannah@gmail.com'
    url = "http://int-sys.usr.space/hangman/games"
    response = requests.post(url, {'email':email})

    json_obj = response.text
    response_dict = json.loads(json_obj)
    gameId = response_dict['gameId']
    word = response_dict['word']
    guessesLeft = response_dict['guessesLeft']

    print len(word), gameId, word, guessesLeft
    return gameId



def play_game(gameId):
    """Play hangman game given gameID from start_game."""

    character = choose_character()
    url="http://int-sys.usr.space/hangman/games/" + gameId + "/guesses"
    response = requests.post(url, {'char':character})

    json_obj = response.text
    response_dict = json.loads(json_obj)

    word = response_dict['word']
    guessesLeft = response_dict['guessesLeft']
    active = response_dict['active']
    msg = response_dict['msg']

    return word



def check_status(gameId):
    """Check the status of a game. """

    url="http://int-sys.usr.space/hangman/games/" + gameId
    response = requests.post(url)

    json_obj = response.text
    response_dict = json.loads(json_obj)
    gameId = response_dict['gameId']
    word = response_dict['word']
    guessesLeft = response_dict['guessesLeft']
    active = response_dict['active']

    return active




gameId1 = start_game()
print play_game(gameId1)




