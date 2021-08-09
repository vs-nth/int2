class WordFrequency:
    def __init__(self, word: str, frequency: int):
        """
        inits
        :param word:
        :param frequency:
        """
        self._word = word
        self._frequency = frequency

    def get_word(self):
        return self._word

    def get_frequency(self):
        return self._frequency

    def __eq__(self, other):
        if self.word == other.word and self.frequency == other.frequency:
            return True
        return False

    def __repr__(self):
        return f"({self._word}, {self._frequency})"

    def __iter__(self):
        # to convert into dict
        yield self._word
        yield self._frequency

    word = property(get_word)
    frequency = property(get_frequency)



