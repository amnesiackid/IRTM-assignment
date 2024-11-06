import csv
import re

class InvertedIndex:

    def __init__(self):
        #initialize the object, store the postings lists in a separate library
        self.dict = {}
        self.postinglst = {}

    def normalize(self, text):
        # normalize and tokenize text
        text = text.lower()  # convert to lowercase
        words = text.split()  # extract words
        return words

    def index(self, path: str):
        with open (path, mode = 'r', encoding= 'utf-8') as file:
            reader = csv.reader(file, delimiter='\t') #treat each tab character as the boundary between columns
            for line in reader:
                # extract tweet id and terms from each line
                tweet_id, user_handle, user_name, tweet_text = line
                terms = self.normalize(tweet_text)
                for term in set(terms):# create set to remove duplicate terms
                    if term not in self.dict:
                    # if the term is new, create a new entry
                        self.dict[term] = {'term' : term, 'postings_lst' : [], 'pointer' : 0} 
                        self.postinglst[term] = []
                    else:
                    # if the entry exists, update postings lists 
                        self.dict[term]['posting_lst'].append(tweet_id)
                        self.dict[term]['pointer']
                        self.postinglst[term].append(tweet_id)

    # define one term query method
    def query(self, term: str):
        # return the corrisponding postings lists of the query term
        return self.postinglst[term]
    
    # define an intersection algorithm
    def intersection(self, term1, term2):
        intersect_lst = []
        # create iterator from the two postings lists
        iterator_term1 = iter(self.query(term1))
        iterator_term2 = iter(self.query(term2))
        # store the initial posting in id1, id2 
        id1 = next(iterator_term1)
        id2 = next(iterator_term2)
        while True:

            try:
                if id1 == id2:
                    # when they occur in a same tweet, store the tweet id
                    intersect_lst.append(next(iterator_term1))
                elif id1 < id2:
                    # If id1 is smaller, advance iterator_term1
                    id1 = next(iterator_term1)
                elif id2 > id1:
                    # If id2 is smaller, advance iterator_term2
                    id2 = next(iterator_term2)
            except StopIteration:
            # end the loop if either iterator is exhausted
                break

        return intersect_lst
    
    # define one term query method
    def query(self, term1, term2):
        # run intersection algorithm and return its result
        return self.intersection(term1, term2)
