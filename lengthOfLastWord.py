# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word in the string.

def lengthOfLastWord(s):
    spaces = 0
    idx = 0
    lenLast = 0
    for i in range(len(s)):
        if s[i] == ' ':
            spaces += 1
            idx = i

            lenLast = len(s) - idx - 1
        elif ' ' not in s:
            lenLast = len(s)

    return lenLast

