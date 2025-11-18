# your code goes here!
class Anagram :
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word.lower())  # store sorted lowercase letters

    def match(self, candidates):
        return [
            candidate
            for candidate in candidates
            if candidate.lower() != self.word.lower() and sorted(candidate.lower()) == self.sorted_word
        ]