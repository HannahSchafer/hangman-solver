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
    word_length = len(word)
    # guessesLeft = response_dict['guessesLeft']

    # print len(word), gameId, word, guessesLeft
    return gameId


def check_status(gameId):
    """Check the status of a game. """

    url="http://int-sys.usr.space/hangman/games/" + gameId
    response = requests.get(url)

    json_obj = response.text
    # print json_obj
    response_dict = json.loads(json_obj)
    gameId = response_dict['gameId']
    # word = response_dict['word']
    # guessesLeft = response_dict['guessesLeft']
    status = response_dict['status']

    return response_dict


# def choose_character():
#     """Choose character to send to 'play_game' function."""


#     word_list = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm', 'p', 'd', 'u', 'c', 'l', 's', 'n', 't', 'o', 'i', 'r', 'a', 'e']
#     return word_list.pop()

#     #if letter in seen set, go to next




def play_game(gameId):
    """Play hangman game given gameID from start_game."""

    status_response = check_status(gameId)
    print status_response

    status = status_response['status']
    print status

    
    letter_list = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm', 'p', 'd', 'u', 'c', 'l', 's', 'n', 't', 'o', 'i', 'r', 'a', 'e']

    while status == 'active':
        # letter_list = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm', 'p', 'd', 'u', 'c', 'l', 's', 'n', 't', 'o', 'i', 'r', 'a', 'e']

        character = letter_list.pop()
        print character
        url="http://int-sys.usr.space/hangman/games/" + gameId + "/guesses"
        response = requests.post(url, {'char':character})
        

        json_obj = response.text
        response_dict = json.loads(json_obj)
        print response_dict
        
        status_response = check_status(gameId)
        status = status_response['status']
        print status
        # print response_dict['word']
        # print response_dict['guessesLeft']




    # print '99999999'
    # print response_dict
    # print response_dict['word']
    # word = response_dict['word']
    # guessesLeft = response_dict['guessesLeft']
    # status = response_dict['status']
    # msg = response_dict['msg']

        # return response_dict


gameId = start_game()
print play_game(gameId)


def master_game():
    """Plays game from start to finish when called."""

    gameId = start_game()


    status_response = check_status(gameId)
    print status_response

    status = status_response['status']
    print status



    while status == 'active':

        play_response = play_game(gameId)
        print play_response
        print play_response['word']

        # word = play_response['word']
        # print word

        # guesses_left = play_response['guessesLeft']
        # print guesses_left

        # status = status_response['status']
        # print status
    #     
        

# master_game()
# gameId = start_game()
# print play_game(gameId)

