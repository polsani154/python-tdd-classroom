class StringExercise:
    def __init__(self):
        pass  # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        try:
            if vowels.index(character) >= 0:
                return True
        except:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest_word = ""
        words = sentence.split(" ")
        for word in words:
            if len(longest_word) < len(word):
                longest_word = word
        return longest_word

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        words_length = []
        words = text.split(" ")
        for word in words:
            words_length.append(len(word))
        return words_length
