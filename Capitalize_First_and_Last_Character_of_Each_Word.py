#You are given a string s consisting of one or more words separated by single spaces. Your task is to capitalize the first and last character of each word in the string.
#If a word contains only one character, capitalize that character.
#Return the transformed string after applying the operation to all words.

class Solution:
    def capitalize_first_last(self, s: str) -> str:
        # Your code goes here
        words = s.split()
        new_words=[]
        for i in words:
            if len(i)==1:
                new_words.append(i.upper())
            else:
                k=i[0].upper()
                l=i[len(i)-1].upper()
                new_words.append(k+i[1:(len(i)-1)]+l)
        return ' '.join(new_words)
