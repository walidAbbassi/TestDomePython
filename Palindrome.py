"""A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, is_palindrome("Deleveled") should return True as character case should be ignored,
resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

https://www.testdome.com/questions/python/palindrome/7962?visibility=1&skillId=9
"""

class Palindrome:

    @staticmethod
    def is_palindrome(word):
        return word.lower() == word[::-1].lower()

print(Palindrome.is_palindrome('Deleveled'))