from unittest import mock

from src import WordFrequencyAnalyzer, WordFrequency
import src

class TestWordFrequencyAnalyzer:

    def test_clean_text(self):
        word = WordFrequencyAnalyzer.clean_text('asd7asd\r\nvq12ggn sdf, s.fg ')
        assert word == ['asd', 'asd', 'vq', 'ggn','sdf', 's', 'fg']

    def test_calculate_all_frequency(self):
        with mock.patch('src.WordFrequencyAnalyzer.clean_text',
                        return_value=['the', 'sun', 'shines', 'over','the', 'lake']):
            word_obj = WordFrequencyAnalyzer()
            text = 'The sun shines over the lake'
            word_obj.calculate_all_frequency(text)
            count = {}
            for word in text.split():
                word = word.lower()
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
            assert word_obj.word_count_hashmap == count

    def test_calculate_highest_frequency(self):
        text = 'a b2b'
        word_obj = WordFrequencyAnalyzer()
        word_obj = word_obj.calculate_highest_frequency(text)
        assert word_obj == 2

    def test_calculate_frequency_for_word(self):
        with mock.patch('src.WordFrequencyAnalyzer.clean_text',
                        return_value=['the', 'sun', 'shines', 'over','the', 'lake']):
            text = 'The sun shines over the lake'
            word_obj = WordFrequencyAnalyzer()
            word_obj = word_obj.calculate_frequency_for_word(text, 'sun')
            assert word_obj == 1

    def test_calculate_most_frequent_n_words_simple(self):
        with mock.patch('src.WordFrequencyAnalyzer.calculate_all_frequency', return_value=None):
            text = 'The sun shines over the lake'
            word_obj = WordFrequencyAnalyzer()
            word_obj.word_count_hashmap = {'the': 2}
            word_obj = word_obj.calculate_most_frequent_n_words(text, n=1)
            output = [WordFrequency('the', 2)]
            assert word_obj == output

    def test_calculate_most_frequent_n_words_complex(self):
        with mock.patch('src.WordFrequencyAnalyzer.calculate_all_frequency', return_value=None):
            text = 'The sun shines over the lake'
            word_obj = WordFrequencyAnalyzer()
            word_obj.word_count_hashmap = {'the': 2, 'lake' : 1, 'over' : 1, 'sun' : 1}
            word_obj = word_obj.calculate_most_frequent_n_words(text, n=4)
            output = [WordFrequency('the', 2), WordFrequency('lake', 1), WordFrequency('over', 1), WordFrequency('sun', 1)]
            assert word_obj == output
