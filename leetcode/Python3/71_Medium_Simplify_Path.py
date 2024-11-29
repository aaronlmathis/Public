"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current drectory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation:
The trailing slash should be removed.

Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:
Multiple consecutive slashes are replaced by a single one.

Example 3:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level (the parent directory).

Example 4:
Input: path = "/../"
Output: "/"
Explanation:
Going one level up from the root directory is not possible.

Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation:

"..." is a valid name for a directory in this problem.
"""
from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Declare a list to use as a stack
        stack = []
        # use str.split() to split the string using '/' as the separator
        pathList = path.split('/')

        # Iterate through directories in pathList
        for dr in pathList:
            # If directory is .. and there is something to the left of it, remove what's to the left of it.
            if dr == '..' and len(stack) > 0:
                stack.pop()
            # If dr is not .. and is also not empty or '.', append it to stack as it is a valid directory.
            elif dr != '' and dr != '.' and dr != '..':
                stack.append(dr)
        # Declare newPath as the new path to return
        newPath = ''
        # Iterate through stack, adding '/' + directory to the newPath
        for p in stack:
            newPath += ('/' + p)
        
        # If Newpath isn't empty, return it, otherwise return '/'
        return newPath if newPath != "" else "/"






            


sol = Solution()
"""
paths = [ 
        ["/home/","/home"],
        ["/home//foo/","/home/foo"],
        ["/home/user/Documents/../Pictures","/home/user/Pictures"],
        ["/../","/"],
        ["/.../a/../b/c/../d/./","/.../b/d"]
    ]
for i, (input, output) in enumerate(paths):
    actual = sol.simplifyPath(input)
    passed = actual == output
    print(f"Example {i+1}: Input: {input}\nExpected Output: {output}\nActual Output: {actual}\nPassed: {passed}\n\n")
"""
path = "/Z/Iyy/HSyT/ItVqc/.././//Z/.././.././../a/gK/../ZurH///x/../////././../.."
print(sol.simplifyPath(path))