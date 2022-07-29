class WordList:
    """Searchable list of words from a file.

    This isn't Boggle-specific (you could use it for Scrabble or other word
    games), so there's no Boggle-specific logic in it.
    """

    def __init__(self, dict_path="dictionary.txt"):
        """Create a word list from a dictionary file on disk.

            >>> wl = WordList("test_dictionary.txt")
            >>> wl.words == {'CAT', 'DOG'}
            True
        """

        self.words = self._read_dict(dict_path)

    #returns stringify JSON? representation of an object
    def __repr__(self):
        return f"<WordList len={len(self.words)}>"

    def _read_dict(self, dict_path):
        """Read dictionary file at dict_path and return set of words."""
        #{word1, word2, word3, word4}
        dict_file = open(dict_path)
        words = {w.strip().upper() for w in dict_file}
        dict_file.close()

        return words

    def check_word(self, word):
        """Is word in word list? if we typed the word is it in the set
         going to test if word is in test_dictionary
         invoke the function check_word("CAT")
         True
         >>> wl = WordList("test_dictionary.txt")
         >>> wl.check_word("CAT")
         True

         invoke the function check_word("PYKAFG")
         False
        >>> wl.check_word("dog")
        False"""

        return word in self.words


english_words = WordList("dictionary.txt")
