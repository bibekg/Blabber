#extra libraries used
import queue
import tools
import random

"""
markov_chain class is a class that creates a(n) markov chain statistical
model on an inputted list of objects.

The class is then able to generate randomly a new list of objects based
on the analysis model of the inputted list.
"""
class markov_chain:
    
    """
    Class constructor, at the very minium, the class needs an inputted list of
    objects the level parameter is extra to specify the level of the markov
    chain
    """
    def __init__(self, obj_list, level):
        self.level = level #level class variable
        self.obj_list = obj_list #list of objects
        self.pair_tb = {}
        self.generate_prob_table()
        
        #TODO: add any more variables/data structs that you need(hint: you do) 
        #will probably need a probability/count table

        #TODO: call generate_probability_table here as well, as that generates
        #probability table to be used later on

    """
    generate_prob_table goes through the list of objects and generates a probability
    table of current object to the previous object that can be used to look up again.
    
    NOTE: you might not need to keeptrack of a probability, just the count of one 
    object appearing after another
    """

    def generate_prob_table(self):
        cache = queue.Queue()

        #first fix method

        # #populates cache for the beginning
        # for i in range(2):
        #     cache.put(self.obj_list[i])

        for word in self.obj_list:
            if cache.qsize() == self.level + 1:

                # Create temporary tuple that holds cache's current value
                # to_input = list(cache)
                # to_input = tuple(to_input)

                to_input = []
                for i in range(cache.qsize()):
                    to_input.append(cache.get())

                for i in range(len(to_input)):
                    cache.put(to_input[i])

                to_input = tuple(to_input)

                # If the key is in the outer dictionary...
                if to_input[0:self.level] in self.pair_tb:

                    # If the output string is in the specific inner dictionary chosen by the tuple key...
                    if to_input[self.level] in self.pair_tb[tuple(to_input[0:self.level])]:
                        # Increment that key's output string's count by 1.
                        self.pair_tb[tuple(to_input[0:self.level])][to_input[self.level]] += 1

                    # If the output string is NOT in the specific inner dictionary chosen by the tuple key...
                    else:
                        # # Create a count for that key's output string and set it equal to 1.
                        self.pair_tb[tuple(to_input[0:self.level])][to_input[self.level]] = 1

                # If the key is not in the outer dictionary...
                else:
                    # Initialize an inner dictionary with key being the input tuple
                    self.pair_tb[tuple(to_input[0:self.level])] = {}
                    # Set that inner dictionary's value to be 1
                    self.pair_tb[tuple(to_input[0:self.level])][to_input[self.level]] = 1

                # Get rid of the first word in the queue
                cache.get()
            # Put in the next word into the queue
            cache.put(word)

    #TODO create a data structure(dictorary of tuples of pairs to count)
    #SHOULD be a class variable so you can reuse later on

    #TODO go through the list of objects stored by the class
        #and record the count of an object appearing after another

    #TODO to implement an n-th degree markov chain, you will need additional
    #data structures to cache up the history(a sequence of previous objects)


    """
    generate_random_list uses the probability table and returns a list of
    objects that adheres to the probability table generated in the previous
    method
    NOTE: the first object has to be selected randomly(the seed)
    NOTE: the count parameter is just to specify the length of the generated
    list
    """
    def generate_obj_list(self, count):

        sentence_list = []
        counter = 0

        firstWord = tools.generateFirstWord(self.pair_tb)

        # Adds the first word to the sentence_list
        for i in range (self.level):
            sentence_list.append(firstWord[i])

        # Adds every word after that for remaining number of necessary times
        for i in range (count - self.level):
            sentence_list.append(tools.weighted_choice(self.pair_tb, tuple(sentence_list[i:i+self.level])))

        return sentence_list



    #TODO generate a random object from the original list(using random)
    #note, to make it truly random, you'll need to use a set of the original
    #list as there might be repeats

    #TODO look up in the probability table generated earlier for the entry of
    #that object. If there are more than one object that pairs with this entry,
    #apply a weighted algorithm based on the count recording(this is why keeping
    #track of count rather than percentage is easier

    #TODO repeat until you from a count length list. NOTE: for an nth level
    #markov chain you will need to look up on the probability an n-length tuple
    #once you've generated enough words!