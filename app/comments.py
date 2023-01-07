"""
Strip Comments
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def strip_comments(strng, markers):
    if len(markers) > 0:
        my_list = strng.split('\n')
        for element in markers:
            my_list = list(map(lambda c: c.split(element)[0].rstrip() + '\n', my_list))
        result = ''.join(my_list)
        return result[:-1]
    else:
        return strng
