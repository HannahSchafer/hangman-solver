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
    """Gets all possible words by word length via nltk corpus of all English words."""

    word_list = []
    # NLTK's dictionary of all words in English
    all_words = words.words('en')
    for wor in all_words:
        if len(wor) == word_length and wor[0].islower():
            word_list.append(wor)

    return word_list



def start_game():
    """Start hangman game."""

    email = 'schafer.hannah@gmail.com'
    url = "http://int-sys.usr.space/hangman/games"
    response = requests.post(url, {'email':email})

    json_obj = response.text
    response_dict = json.loads(json_obj)
    gameId = response_dict['gameId']
    # word = response_dict['word']
    
    
    return gameId



def check_status(gameId):
    """Check the status of a game. """

    # connect to check_status API
    url="http://int-sys.usr.space/hangman/games/" + gameId
    response = requests.get(url)

    json_obj = response.text
    response_dict = json.loads(json_obj)

    return response_dict




def play_game(gameId):
    """Play hangman game given gameID from start_game."""

    status_response = check_status(gameId)
    status = status_response['status']

    seen = set()
    start_letter = ['q', 'j', 'z', 'x', 'v', 'k', 'w', 'y', 'f', 'b', 'g', 'h', 'm', 'p', 'd', 'u', 'c', 'l', 's', 'n', 't', 'o', 'i', 'r', 'a', 'e']
    character = start_letter.pop()

    while status == 'active':

    
        seen.add(character)
        print seen
        
        # connecting to play_game API
        url="http://int-sys.usr.space/hangman/games/" + gameId + "/guesses"
        response = requests.post(url, {'char':character})
        
        json_obj = response.text
        response_dict = json.loads(json_obj)
        print response_dict

        if 'word' in response_dict:
            word = response_dict['word']
            print word
            print '77777777'

            word_length = len(word)
            print word_length
            word_list = possible_words(word_length)


            # list of lists, containing known letter and letter's index in word
            idx_letters = []
            for i, let in enumerate(word):
                if let.isalpha():
                    idx_letters.append([i, let])

            if len(idx_letters) > 0:
                # narrows down potential words by matching index and letter from those already known
                potentials = []
                for w in word_list:
                    for i, char in enumerate(w):
                        for item in idx_letters:
                            if item[0] == i and item[1] == char:
                                potentials.append(w)
                # setting new (narrowed) word list    
                word_list = potentials
                print len(word_list)

                # find most common letters among list of potenital words
                counter = Counter(chain.from_iterable(imap(set, word_list)))
                most_common_lets = map(itemgetter(0), counter.most_common())
                print 'most common letters:', most_common_lets

                # send most common letter from potentials to game to play, that has not already been played
                print 'seen:', seen
                j=0
                while most_common_lets[j] in seen:
                    j += 1
                    # print most_common_lets[j]
                    

                character = most_common_lets[j]
            
            
   
    
        status_response = check_status(gameId)
        status = status_response['status']
        print status
        

    return response_dict['msg']


    
gameId = start_game()
print play_game(gameId)


