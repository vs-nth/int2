class WordFrequency:

    # word: str
    # frequency: int

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

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __repr__(self):
        return f"{self._word}: {self._frequency}"

    word = property(get_word)
    frequency = property(get_frequency)



