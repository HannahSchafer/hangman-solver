# encoding=utf8  
import nltk
nltk.download('words')
from nltk.corpus import words
import requests
import json
from collections import Counter
from itertools import chain, imap
from operator import itemgetter


# def word_length_buckets():
#     """Sorts all English words into dictionary, where key is word length."""

#     word_list = words.words('en')
#     print word_list[:15]

#     #236,736 words total
#     # print len(word_list)

#     # word_length_dict = {}
#     # for word in word_list:
#     #     if word[0].islower():
#     #         word_length_dict.setdefault(len(word),[]).append(word)

#     return word_length_dict

# print word_length_buckets()

    
def possible_words(word_length):

    word_list = []
    # NLTK's dictionary of all words in English
    all_words = words.words('en')
    for word in all_words:
        if len(word) == word_length and word[0].islower():
            word_list.append(word)

    return word_list




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
    
    return gameId



def check_status(gameId):
    """Check the status of a game. """

    url="http://int-sys.usr.space/hangman/games/" + gameId
    response = requests.get(url)

    json_obj = response.text
    # print json_obj
    response_dict = json.loads(json_obj)
    # gameId = response_dict['gameId']
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

    word = status_response['word']
    word_length = len(word)
    print word_length

    word_list = possible_words(word_length)

    letter_list = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm', 'p', 'd', 'u', 'c', 'l', 's', 'n', 't', 'o', 'i', 'r', 'a', 'e']
    character = letter_list.pop()

    while status == 'active':
        # letter_list = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm', 'p', 'd', 'u', 'c', 'l', 's', 'n', 't', 'o', 'i', 'r', 'a', 'e']

        seen = {}
        print character
        url="http://int-sys.usr.space/hangman/games/" + gameId + "/guesses"
        response = requests.post(url, {'char':character})
        

        json_obj = response.text
        response_dict = json.loads(json_obj)
        print response_dict
        word = response_dict['word']
        print word

        # list of lists, containing known letter and letter's index in word
        idx_letters = []
        for i, let in enumerate(word):
            if let.isalpha():
                idx_letters.append([i, let])

        if len(idx_letters) > 0:

            # narrows down potential words by matching index and letter from those already known
            potentials = []
            for word in word_list:
                for i, char in enumerate(word):
                    for item in idx_letters:
                        if item[0] == i and item[1] == char:
                            potentials.append(word)
            # setting new (narrowed) word list    
            word_list = potentials
            print len(word_list)

            # find most common letters among list of potenital words
            counter = Counter(chain.from_iterable(imap(set, word_list)))
            print '9999999'
            most_common_lets = map(itemgetter(0), counter.most_common())
            print most_common_lets
            print '9999999'

            # send most common letter from potentials to game to play, that has not already been played
            j=0
            while most_common_lets[j] in seen:
                j += 1

            character = most_common_lets[j]
            
    
        status_response = check_status(gameId)
        status = status_response['status']
        print status
        # print response_dict['word']
        # print response_dict['guessesLeft']

    return response_dict['msg']


    
gameId = start_game()
print play_game(gameId)


