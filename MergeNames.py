"""Implement the unique_names method. When passed two arrays of names,
it will return an array containing the names that appear in either or both arrays.
The returned array should have no duplicates.

For example, calling MergeNames.unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
should return an array containing Ava, Emma, Olivia, and Sophia in any order.

https://www.testdome.com/questions/python/merge-names/21508
"""

class MergeNames:

    @staticmethod
    def unique_names(names1, names2):
        return list(set(names1 + names2))

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(MergeNames.unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia