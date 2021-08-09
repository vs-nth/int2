

from src import WordFrequency


class TestWordFrequency:

    def test_instance(self):
        word = WordFrequency('a', 3)
        output = str
        for _ in word:  # test iterable
            output = str(word)
        assert output == '(a, 3)'
