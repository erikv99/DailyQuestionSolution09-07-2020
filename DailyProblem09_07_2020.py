# Given a string, find the length of the longest substring without repeating characters

class Solution:
  
    def lengthOfLongestSubstring(self, string):
        
        alreadyUsedChars = ""
        longestSubString = 0
        currentSubLength = 0

        # Looping thru all the chars in the given string
        for char in string:

            # Checking if the current char is already in our alreadyUsedChar string
            if (char in alreadyUsedChars):

                # Checking if this substring is longer then the current biggest substring
                if (currentSubLength > longestSubString):

                    # Setting the current sub string length as the longest length
                    longestSubString = currentSubLength

                    # Reseting the alreadyUsedChars string and currentSubLength
                    alreadyUsedChars = ""
                    currentSubLength = 0

            # If the current char is not already used 
            else: 

                # Incrementing the current substring length
                currentSubLength += 1
                # Adding the current char to our alreadyUsedChars 
                alreadyUsedChars += char

        # Returning the result
        return longestSubString


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10