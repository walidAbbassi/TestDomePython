"""Anonymous
Write a function that, given a list and a target sum, returns zero-based indices of any two distinct elements whose sum is equal to the target sum. If there are no such elements, the function should return (-1, -1).

For example, find_two_sum([1, 3, 5, 7, 9], 12) should return a tuple containing any of the following pairs of indices:

1 and 4 (3 + 9 = 12)
2 and 3 (5 + 7 = 12)
3 and 2 (7 + 5 = 12)
4 and 1 (9 + 3 = 12)

https://www.testdome.com/questions/python/two-sum/14289
"""

class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """
        dict = {}
        for i in range(len(numbers)):
            # dict[numbers[i]] = i
            # print (dict)
            if target_sum - numbers[i] in dict.keys() and dict[target_sum - numbers[i]] != i:  # ensure not itself; [2,5,4] sum=10 should be false
                return (dict[target_sum - numbers[i]], i)
            dict[numbers[i]] = i  # should be here; incase [5,5] return false
        return None

    @staticmethod
    def find_two_sum2(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """
        dict = {}
        for count, value in enumerate(numbers):
            try:
                return (dict[value], count)
            except KeyError:
                dict[target_sum - value] = count
        return (-1, -1)


print(TwoSum.find_two_sum([1, 3, 5, 7, 9], 12))
print(TwoSum.find_two_sum2([1, 3, 5, 7, 9], 12))
