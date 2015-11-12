__author__ = 'bibek'
'''
weighted_random module makes it easier to do weighted random
'''
import random
import string

#weighted choices takes in a dictionary of choices to weight
#and returns randomly a choice given by weights(ints)
def weighted_choice(weights, curr_word):
    #TODO: stupid way to doing this, I know
    m_list = []

    # curr_word is the origin word passed into function
    # obj corresponds to each second word
    for obj in weights[curr_word]:
        # times corresponds to count of second word
        for times in range(weights[curr_word][obj]):
                m_list.append(obj)
    return random.choice(m_list)

#removes punctuation from a string

def generateFirstWord(weights): # weights is the input dictionary we're generating random first word from
    m_list = []
    # for each tuple of n-level words in the main dictionary
    for obj in weights:
        # for each output string in that given tuple
        for obj2 in weights[obj]:
            # for the appearance count of that output string
            for times in range(weights[obj][obj2]):
                # add that tuple to m_list
                m_list.append(obj)

    # return a random tuple from that list
    return random.choice(m_list)

#TODO: understand why this is fastest
def strip_punctuation(s):
    return s.translate(s.maketrans("","", string.punctuation))