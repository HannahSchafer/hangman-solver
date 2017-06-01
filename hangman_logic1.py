# encoding=utf8  
import nltk
nltk.download('words')
from nltk.corpus import words
import requests
import json
from collections import Counter
from itertools import chain, imap
from operator import itemgetter


    
def possible_words(word_length):
    """Gets all possible words by word length via nltk corpus of all English words.
       Used as helper function in play_game function."""

    word_list = []
    # NLTK's dictionary of all words in English
    all_words = words.words('en')
    for wor in all_words:
        if len(wor) == word_length and wor[0].islower():
            word_list.append(wor)

    return word_list



def compare_letters(word):
    """Compares known letters/indexes in game word with letters/indexes from 
       list of possible words."""

    # list of lists, containing known letter and letter's index in word
    idx_letters = []
    for i, let in enumerate(word):
        if let.isalpha():
            idx_letters.append([i, let])

    return idx_letters



def start_game():
    """Start hangman game and return gameId."""

    email = 'schafer.hannah@gmail.com'
    url = "http://int-sys.usr.space/hangman/games"
    response = requests.post(url, {'email':email})

    json_obj = response.text
    response_dict = json.loads(json_obj)
    gameId = response_dict['gameId']
    
    return gameId



def check_status(gameId):
    """Check the status of a game."""

    # connect to check_status API
    url="http://int-sys.usr.space/hangman/games/" + gameId
    response = requests.get(url)

    json_obj = response.text
    response_dict = json.loads(json_obj)
    status = response_dict['status']

    return status



def play_game(gameId):
    """Play hangman game given gameId from start_game."""

    # initialize status for use as while loop condition
    status = check_status(gameId)

    seen = set()

    # most freuqently used letters in English, in reverse order (to pop from the end)
    start_letter = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm', 'p', 'd', 'u', 'c', 'l', 's', 'n', 't', 'o', 'i', 'r', 'a', 'e']
    character = start_letter.pop()


    while status == 'active':
    
        seen.add(character)
        
        # connecting to play_game API
        url="http://int-sys.usr.space/hangman/games/" + gameId + "/guesses"
        response = requests.post(url, {'char':character})
        
        json_obj = response.text
        response_dict = json.loads(json_obj)
        print response_dict

        if 'word' in response_dict:
            word = response_dict['word']
            word_length = len(word)
            
            # helper function to bring in list of all possible words based on word_length
            word_list = possible_words(word_length)

            # helper function to compare game word to possible words
            idx_letters = compare_letters(word)

            # narrow down potential words by matching index and letter from those already known
            if len(idx_letters) > 0:
                potentials = []
                for w in word_list:
                    for i, char in enumerate(w):
                        for item in idx_letters:
                            if item[0] == i and item[1] == char:
                                potentials.append(w)

                # re-setting new (narrowed) word list in each iteration   
                word_list = potentials

                # find most common letters among list of potenital words
                counter = Counter(chain.from_iterable(imap(set, word_list)))
                most_common_lets = map(itemgetter(0), counter.most_common())

                # send most common letter not already played to play_game API
                j=0
                while most_common_lets[j] in seen:
                    j += 1

                # new character to play 
                character = most_common_lets[j]

                # check status to see if allowed another guess or if break from while loop
                status = response_dict['status']
                print 'play status', status

        # continue going through start_letter list until find a letter to begin with    
        elif 'word' not in response_dict and status == 'active':
            character = start_letter.pop()


    return response_dict
        

    
# gameId = start_game()
# print play_game(gameId)


