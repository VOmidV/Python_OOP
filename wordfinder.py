"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file):
        files = open(file)
        self.word = self.count_word(self.files)
        print(f'{len(self.word)} words read')

    def count_word(self, files):
        return [val.strip() for val in files]

    def random(self):
        return random.choice(self.word)
    

class SpecialWordFinder(WordFinder):
    def count_word(self, dict_file):
        return [val.strip() for val in dict_file
                if val.strip() and not val.startswith("#")]

    