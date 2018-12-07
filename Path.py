"""Write a function that provides change directory (cd) function for an abstract file system.

Notes:

Root path is '/'.
Path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters (A-Z and a-z).
The function should support both relative and absolute paths.
The function will not be passed any invalid paths.
Do not use built-in path-related functions.
For example:

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
should display '/a/b/c/x'."""

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        current_path = [value for value in self.current_path.split('/')]
        new_pathList = [value for value in new_path.split('/')]
        print(current_path)
        for count , value in enumerate(new_pathList):
            if(value == '..'):
                current_path.pop()
            else:
                current_path.append(new_pathList[count])
        self.current_path = ("/".join(current_path))

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)