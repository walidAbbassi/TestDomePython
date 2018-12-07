"""Hazael Gomez
Implement the find_common method. When passed two arrays of names, it will return an array containing
the names that appear in either or both arrays. The returned array should have no duplicates.

For example, calling CommonNames.find_common(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
should return an array containing Ava, Emma, Olivia, and Sophia in any order.

https://www.testdome.com/questions/python/common-names/20302?visibility=1
"""

class CommonNames:

    @staticmethod
    def find_common(names1, names2):
        return sorted(list(set(names1+names2)))

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(CommonNames.find_common(names1, names2)) # should print Ava, Emma, Olivia, Sophia