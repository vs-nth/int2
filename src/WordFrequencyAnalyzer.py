from typing import List
from src import WordFrequency
import re
import bisect
import collections


class WordFrequencyAnalyzer:

    def __init__(self):
        self.word_count_hashmap = dict

    @staticmethod
    def clean_text(text: str) -> list:
        text = re.findall('[a-zA-Z]+', text)  # regex to extract only words [a-zA-Z]+
        return [_.lower() for _ in text]

    def calculate_all_frequency(self, text: str) -> None:
        """
        calculates the frequency of the given text
        :param text: text in which frequency is to be calculated
        """
        text = self.clean_text(text)
        self.word_count_hashmap = collections.Counter(text)

        # If not allowed to use inbuilt function - the above line can be replaced with these:
        # count = {}
        # for word in text:
        #     word = word.lower()
        #     if word in count:
        #         count[word] += 1
        #     else:
        #       count[word] = 1
        # self.word_count_hashmap = count

    def calculate_highest_frequency(self, text: str) -> int:
        """
        Returns the highest frequency in text
        :param text: the text in which to count the words
        :return: highest frequency of occurrence
        """
        self.calculate_all_frequency(text)
        return max(self.word_count_hashmap.values())

    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        """
        Calculates the frequency of given word in the input text
        :param text: text in which to search
        :param word: the word to count in the input text
        :return: word_count: the frequency of occurrence of the word in the text
        """
        text = self.clean_text(text)
        return text.count(word)

    def calculate_most_frequent_n_words(self, text: str, n: int) -> List[WordFrequency]:
        """
        Calculates and returns the top 'n' most frequently occurring words
        :param text: text in which to search
        :param n: n words to return
        :return: list[wordFrequency] returns a list with n WordFrequency objects
        """
        self.calculate_all_frequency(text)
        most_frequent_n_words = []
        reverse_word_count_hashmap = {}
        count = 0
        for word, frequency in self.word_count_hashmap.items():
            if frequency not in reverse_word_count_hashmap:
                reverse_word_count_hashmap[frequency] = [word]
            else:
                bisect.insort(reverse_word_count_hashmap[frequency], word)
        while count < n:
            val = max(reverse_word_count_hashmap)
            for word in list(reverse_word_count_hashmap[val]):
                most_frequent_n_words.append(WordFrequency(word, val))
                reverse_word_count_hashmap[val].remove(word)
                count += 1
                if not reverse_word_count_hashmap[val]:
                    reverse_word_count_hashmap.pop(val)
                if count > n:
                    most_frequent_n_words.pop()
                    count -= 1
        return most_frequent_n_words




