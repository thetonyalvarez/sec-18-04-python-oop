"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """returns a random word from a text file

    >>> wf = WordFinder("test.txt")
    3 words read

    >>> wf.random() in ["car", "bike", "truck"]
    True

    >>> wf.random() in ["car", "bike", "truck"]
    True

    >>> wf.random() in ["car", "bike", "truck"]
    True

    """

    def __init__(self, filename):
        """read text file and return no. of items in file"""

        self.filename = filename

        file = open(filename)

        self.lst = self.parse(file)
        
        print(f"{len(self.lst)} words read")
        
    def parse(self, file):
        """iterate over items in file and remove leading and trailing characters for each item"""
        
        return [word.strip() for word in file]

    def random(self):
        """return a random item from the list of items"""

        return random.choice(self.lst)

class SpecialWordFinder(WordFinder):
    """special WordFinder that removes blank lines and comments

    >>> wf2 = SpecialWordFinder("testspecial.txt")
    3 words read

    >>> wf2.random() in ["car", "bike", "truck"]
    True

    >>> wf2.random() in ["car", "bike", "truck"]
    True

    >>> wf2.random() in ["car", "bike", "truck"]
    True
    """

    def parse(self, file):
        """iterate over items in file and remove leading and trailing characters, blank lines, and lines that begin with #"""

        return [word.strip() for word in file if word.strip() and not word.startswith("#")]