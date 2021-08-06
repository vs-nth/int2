from typing import List
from WordFrequency import WordFrequency
import re
import bisect
import collections


class WordFrequencyAnalyzer:

    # word: str
    # frequency: int
    word_count_hashmap: dict

    # TODO CANNOT INSERT IN SORTED ORDER IF VALUES ARE NOT FULLY COUNTED YET
    #  create your own counter insert into dict in sorted order itself -> use popitem to evict last (LIFO)
    #  this way you can insert in sorted order into dict itself according to variables, and then when retrieving
    #  you can remove from last .

    @staticmethod
    def clean_text(text: str) -> list:
        text = re.findall('[a-zA-Z]*', text)  # regex to extract only words [a-zA-Z]*
        text = [_ for _ in text if _ != '']  # remove empty spaces
        return text

    # make this function calculate all, make the bottom one return the max value?
    def calculate_all_frequency(self):
        pass

    def calculate_highest_frequency(self, text: str) -> int:
        """
        Returns the highest frequency of occurrence of words
        :param text: the text in which to count the words
        :return: max_count: highest frequency of occurrence
        """
        # TODO make the count into WordFrequency Object? or something?  - reverse hashmap - append subsequent strings with same value into str? idk

        # TODO change to collections.counter after clean_text
        count = {}
        max_count = 0
        # define word using regex - > extract [a-zA-Z]* , ignore rest. check hashmap
        # change these into a function to extract words
        text = self.clean_text(text)
        for word in text:
            word = word.lower()
            if word in count:
                count[word] += 1
                if max_count < count[word]:
                    max_count = count[word]
            else:
                count[word] = 1
        self.word_count_hashmap = count
        return max_count

    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        """
        Calculates the frequency of given word in the input text
        :param text: text in which to search
        :param word: the word to count in the input text
        :return: word_count: the frequency of occurrence of the word in the text
        """
        text = self.clean_text(text)
        return text.count(word)  # verify this -> check if word is only alphabetic

    def calculate_most_frequent_n_words(self, text: str, n: int) -> List[WordFrequency]:
        """
        Calculates and returns the top 'n' most frequently occurring words
        :param text: text in which to search
        :param n: n words to return
        :return: list[wordFrequency] returns a list with n WordFrequency objects
        """
        _ = self.calculate_highest_frequency(text)  # maybe use the _ instead of wasting one max call using a do while loop
        most_frequent_n_words = []
        count = 0
        while count < n:
            val = max(self.word_count_hashmap.values())
            word_list_with_val_freq = []

            # insert all words with same frequency into a list in sorted manner
            for k, v in self.word_count_hashmap.items():
                if v == val:
                    bisect.insort(word_list_with_val_freq, k)

            # create WordFrequency Object for each word, and remove that word from dict
            for i in word_list_with_val_freq:
                if count < n:
                    most_frequent_n_words.append(WordFrequency(i, val))
                    count += 1
                    self.word_count_hashmap.pop(i)

        return most_frequent_n_words


if __name__ == "__main__":
    wew = WordFrequencyAnalyzer()
    f = wew.calculate_most_frequent_n_words(text="The sun shines over the lake", n=3)
    print(f)
    print(dict(f))
    f = wew.calculate_most_frequent_n_words(text="hi this is My m2y 2my2 NaMe name NAME ih2hi kusu kundi,tqw (awqe) (qwerttty) awqe", n=5)
    print(f)





