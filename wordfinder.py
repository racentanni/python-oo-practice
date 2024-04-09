"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''For finding ramdom words from dictinary

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["car", "boat", "airplane" ]
    True

    >>> wf.random() in ["car", "boat", "airplane" ]
    True
    >>> wf.random() in ["car", "boat", "airplane" ]
    True

     '''



    def __init__(self,path):
        
        dict_file = open(path)
        """read dictionary and return number read"""

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")


    def parse (self, dict_file):
        """parse dict_file -> word list"""

        return [w.strip() for w in dict_file]
    
    def random(self):
        """ return random words"""

        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """ Specialized word finder

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["car", "phone", "computer"]
    True

    >>> swf.random() in ["car", "phone", "computer"]
    True

    >>> swf.random() in ["car", "phone", "computer"]
    True
    """

    def parse(self, dict_file):
        """ parse dict_file , listing words, skipping blanks andcomments"""

        return [w.strip() for w in dict_file if w.strip() and not w.startwith("#")]   
    ...
