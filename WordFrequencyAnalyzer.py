from typing import List
from WordFrequency import WordFrequency
import re
import bisect


class WordFrequencyAnalyzer:

    # word: str
    # frequency: int
    word_count_hashmap: dict

    @staticmethod
    def clean_text(text: str) -> list:
        text = re.findall('[a-zA-Z]*', text)  # regex to extract only words [a-zA-Z]*
        text = [_ for _ in text if _ != '']  # remove empty spaces
        return text

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
            val = max(self.word_count_hashmap)
            # for i in [k for k, v in self.word_count_hashmap.items() if v == val]:
            #     count += 1
            word_list_with_val_freq = []

            for k, v in self.word_count_hashmap.items():
                if v == val:
                    bisect.insort(word_list_with_val_freq, k)
            for i in word_list_with_val_freq and count < n:
                most_frequent_n_words.append(WordFrequency(i, val))
                count += 1
                self.word_count_hashmap.pop(i)
            # map(self.word_count_hashmap.pop, word_list_with_val_freq)
            # lambda x: self.word_count_hashmap.pop(x) for x in word_list_with_val_freq
        return most_frequent_n_words



        # dict_of_words = {}
        # dict_of_counts = {}  # hashmap counts to lists of matched words that have same frequency, sort the list?
        #
        # for word in text:
        #     word = word.lower()
        #     if word in dict_of_words:
        #         dict_of_words[word] += 1
        #         if dict_of_words[word] in dict_of_counts:
        #             bisect.insort(dict_of_counts[dict_of_words[word]], word)  # add word in sorted order
        #         else:
        #             dict_of_counts[dict_of_words[word]] = [word]
        #     else:
        #         dict_of_words[word] = 1
        #         if dict_of_words[word] not in dict_of_counts:
        #             dict_of_counts[dict_of_words[word]] = [word]
        #         else:
        #             dict_of_counts[dict_of_words[word]].append(word)
        #
        # print(dict_of_counts, dict_of_words)
        # count = 0
        # while count < n:
        #     val = max(dict_of_counts)
        #     for i, v in enumerate(dict_of_counts[val]):
        #         most_frequent_n_words.append(WordFrequency(v, val))
        #         count += 1
        #         dict_of_counts[val].pop(i)
        #     dict_of_counts.pop(val)




if __name__ == "__main__":
    wew = WordFrequencyAnalyzer.calculate_most_frequent_n_words(text="The sun shines over the lake", n=3)
    print(wew)

