"""Vjekoslav Giacometti
Implement a group_by_owners function that:
Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

https://www.testdome.com/questions/python/file-owners/11846
"""
#Passes 3/3 tests
class FileOwners:

    @staticmethod
    def group_by_owners(files):
        dict = {value:[] for key , value in files.items()}
        for key,value in files.items():
            dict[value].append(key)
        return dict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))