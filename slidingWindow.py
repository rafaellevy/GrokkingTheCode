

from calendar import c
from turtle import right
from unittest import result


def findAverages(array, k):
    # result array holds the averages / k
    result = []
    # startWindowIdx
    startWindow = 0
    # currentSum
    currentSum = 0
    # go through array
    for endWindow in range(len(array)):
        # we sum all endWindows up to a k size
        currentSum += array[endWindow]
        #if we reach the k window size
        if endWindow >= k -1:
            # calculate averages
            result.append(currentSum / k)
            # subtract from the sum element that is about to get out of the window
            currentSum -= array[startWindow]
            # new window will start one index forward
            startWindow += 1
    return result


array = [1,2,3,4,5,6]
k = 2
print(findAverages(array,k))



def findMaxSubSum(array, k):
    # maxSum var keeps track of the max currentSum of all the subarrays
    maxSum = float("-inf")
    #currentSum of the current window, size k
    currentSum = 0
    #windowStartIdx is the idx where the currentWindow start
    windowStart = 0

    # go through the array:
    for windowEnd in range(len(array)):
        # sum all elements to currentSum
        currentSum += array[windowEnd]
        # check if we reach the window sike k
        if windowEnd >= k - 1:
            # update maxSum ( max of all currentSum, possible windows)
            maxSum = max(currentSum, maxSum)
            # subtract the element that is getting out of the next window
            currentSum -= array[windowStart]
            # move windowStart by one so we can have a new window start 
            windowStart += 1

    return maxSum

print(findMaxSubSum([1,2,3,4,5,6,7],3))


def findSmallestSub(array, s):
    # find the smallest subArray that is greater or equal to a given number s
    # return the lenght of the smallest SubArray 
    currentSum = 0
    # keeps the currentSum
    windowStart = 0
    # start of our sliding window
    minimumLength = float("inf")
    
    for windowEnd in range(len(array)):
    # go over the length of input array
        currentSum += array[windowEnd]
        # add numbers to the sum until the sum is equal or greater given number s
        # while currentSum is equal or greater than number s, we shrink the window
        # we update minimumlength if that's the case
        while currentSum >= s:
             #calculate length of window
            windowSize = windowEnd - windowStart + 1
            if windowSize < minimumLength:
                # if currentWindowSize is smaller that minimumLength, update 
                minimumLength = windowSize
            currentSum -= array[windowStart]
            windowStart += 1
           
    if minimumLength == float("inf"):
        return 0        
    return minimumLength

print(findSmallestSub([2, 1, 5, 2, 3, 2],7))
print(findSmallestSub([2, 1, 5, 2, 8],7))
print(findSmallestSub([3, 4, 1, 1, 6],8))




def findLongestSubK(s,k):
    frequency = {}
    longestSub = 0
    currentLongest = 0
    windowStart = 0

    for windowEnd in range(len(s)):
        if s[windowEnd] not in frequency:
            frequency[s[windowEnd]] = 0
        frequency[s[windowEnd]] += 1

        while len(frequency) > k:
            characterToRemove = s[windowStart]
            frequency[characterToRemove] -= 1
            if frequency[characterToRemove] == 0:
                del frequency[characterToRemove]
            windowStart += 1
            currentLongest -= 1

        currentLongest += 1
        longestSub = max(currentLongest, longestSub)

    return longestSub
    
    

       
print(findLongestSubK("cbbebi",3))
print(findLongestSubK("cbbebi",10))
print(findLongestSubK("araaci",1))
print(findLongestSubK("araaci",2))


# Version 2 
def findMaxSubSizeK(s, k):
    letterFrequency = {}
    windowStart = 0
    maxSub = 0

    for windowEnd in range(len(s)):
        if s[windowEnd] not in letterFrequency:
            letterFrequency[s[windowEnd]] = 0

        letterFrequency[s[windowEnd]] += 1

        while len(letterFrequency) > k:
            leftSub = s[windowStart]
            letterFrequency[leftSub] -= 1
            windowStart += 1
            if letterFrequency[leftSub] == 0:
                del letterFrequency[leftSub]
        maxSub = max(maxSub, windowEnd - windowStart + 1)

    return maxSub
            
print("HI ! ! ! ")
print(findMaxSubSizeK("cbbebi",3))
print(findMaxSubSizeK("cbbebi",10))
print(findMaxSubSizeK("araaci",1))
print(findMaxSubSizeK("araaci",2))

def fruitBaskets(a):
    windowStart = 0
    fruitFrequency = {}
    basketSize = 0

    for windowEnd in range(len(a)):
        if a[windowEnd] not in fruitFrequency:
            fruitFrequency[a[windowEnd]] = 0
        fruitFrequency[a[windowEnd]] += 1

        while len(fruitFrequency) > 2:
            leftSub = a[windowStart]
            fruitFrequency[leftSub] -= 1
            if fruitFrequency[leftSub] == 0:
                del fruitFrequency[leftSub]
            windowStart += 1
        basketSize = max(basketSize, windowEnd - windowStart + 1)
    return basketSize

print("fruitBasket")
print(fruitBaskets(['A', 'B', 'C', 'A', 'C']))
print(fruitBaskets(['A', 'B', 'C', 'B', 'B', 'C']))



# we ended up not using sliding window 
def lengthLongestSub(s):
    longest = 0
    #windowStart = 0
    currentSet = set()

    for windowEnd in range(len(s)):
        if s[windowEnd] not in currentSet:
            currentSet.add(s[windowEnd])
        else:
            currentSet = set((s[windowEnd]))
    
        longest = max ( longest, len(currentSet))

    return longest

print("longestSub")
print(lengthLongestSub("abccde"))    


def longestDistinctSubstring(s):
    windowStart = 0
    longest = 0
    lettersIdx = {}

    for windowEnd in range(len(s)):
        rightSub = s[windowEnd]

        if rightSub not in lettersIdx:
            lettersIdx[rightSub] = windowEnd
        else:
            windowStart = max(windowStart, lettersIdx[rightSub] + 1)
            lettersIdx[rightSub] = windowEnd

        longest = max (longest, windowEnd - windowStart + 1 )

    return longest

print("Longest distinc substring")
print(longestDistinctSubstring("aabccbb"))
print(longestDistinctSubstring("abbbb"))
print(longestDistinctSubstring("abccde"))



def longestSubWithReplacement(s,k):
    # where our window starts
    windowStart = 0
    # keep track of the longest possible sub
    maxLength = 0
    # which letter has the higher frequency
    maxFrequency = 0
    # frequency of all letters
    letterFrequency = {}

    for windowEnd in range(len(s)):
        # check if char is in our dictionary
        rightEnd = s[windowEnd]
        if rightEnd not in letterFrequency:
            # create key
            letterFrequency[rightEnd] = 0
        # if it's add 1 to frequency
        letterFrequency[rightEnd] += 1

        # calculate and keep track of the letter with the higher freq.
        # we do that in all iterations for all the characters
        maxFrequency = max(maxFrequency, letterFrequency[rightEnd])

        # now we check if the windowSize if the difference btw our window and the char with higher freq passed the k value
        # meaning we cannot change chars, we should shrink the window

        if (windowEnd - windowStart + 1) - maxFrequency > k:
            # reduce 1 from dictionary 
            letterFrequency[s[windowStart]] -= 1
            # shrink window
            windowStart += 1

        # calculate the maximum length we achieved so far
        maxLength = max(maxLength, windowEnd - windowStart + 1)

    return maxLength

print("longest sub replacing chars")
print(longestSubWithReplacement("aabccbb",2))
print(longestSubWithReplacement("abbcb",1))
print(longestSubWithReplacement("abccde",1))



def longestContiguousSubarrayAll1s(arr,k):
    windowStart = 0
    maxOneFrequency = 0
    maxLength = 0

    for windowEnd in range(len(arr)):
        rightEnd = arr[windowEnd]

        if rightEnd == 1:
            maxOneFrequency += 1
        
        
        if (windowEnd - windowStart + 1) - maxOneFrequency > k:
            leftEnd = arr[windowStart]
            if leftEnd == 1:
                maxOneFrequency -= 1
            windowStart += 1
        
        maxLength = max(maxLength, windowEnd - windowStart + 1)

    return maxLength
    
print("longestSubstringWithAll1s")
print(longestContiguousSubarrayAll1s([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],2))
print(longestContiguousSubarrayAll1s([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],3))


# non sliding window version
def permutationString(s,pattern):
    #create pattern dictionary
    patternFreq = {}
    # strFreq dictionary must match patternFreq dictionary
    strFreq = {}
    for char in pattern:
        if char not in patternFreq:
            patternFreq[char] = 0
        patternFreq[char] += 1

    # go over the input string, if char not in pattern freq, start a new strFreq
    # if char in patternFreq, we create a key for strFreq
    # at the end We compare dictionary
    for char in s:
        if char not in patternFreq:
            if strFreq != patternFreq:
                strFreq = {}
            else:
                return True
        else:
            if char not in strFreq:
                strFreq[char] = 0
            if patternFreq[char] > strFreq[char]:
                strFreq[char] += 1
            
    return strFreq == patternFreq

print("string permutation without sliding window")
print(permutationString("oidbcaf","abc"))
print(permutationString("odicf","dc"))
print(permutationString("bcdxabcdy","bcdyabcdx"))
print(permutationString("aaacb","abc"))

# sliding window version
def permutationString2(s, pattern):
    patterFreq = {}
    windowStart = 0
    matches = 0

    for char in pattern:
        if char not in patterFreq:
            patterFreq[char] = 0
        patterFreq[char] += 1

    for windowEnd in range(len(s)):
        rightChar = s[windowEnd]
        if rightChar in patterFreq:
            patterFreq[rightChar] -= 1
            if patterFreq[rightChar] == 0:
                matches += 1

        if matches == len(patterFreq):
            return True
        
        if windowEnd  >= len(pattern) - 1:
            leftChar = s[windowStart]
            windowStart += 1
            if leftChar in patterFreq:
                if patterFreq[leftChar] == 0:
                    matches -= 1
                patterFreq[leftChar] += 1
            

    return False

print("permutation slinding window")
print(permutationString2("oidbcaf","abc"))
print(permutationString2("odicf","dc"))
print(permutationString2("bcdxabcdy","bcdyabcdx"))
print(permutationString2("aaacb","abc"))

def findAnagrams(str1,pattern):
    frequency = {}
    windowStart = 0
    matched = 0
    result = []

    for char in pattern:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1

    for windowEnd in range(len(str1)):
        rightEnd = str1[windowEnd]

        if rightEnd in frequency:
            frequency[rightEnd] -= 1
            if frequency[rightEnd] == 0:
                matched += 1

        if matched == len(frequency):
            result.append(windowStart)

        if windowEnd >= len(pattern) - 1:
            leftEnd = str1[windowStart]
            if leftEnd in frequency:
                if frequency[leftEnd] == 0:
                    matched -= 1
                frequency[leftEnd] += 1
            windowStart += 1

    return result

print("find anagrams")
print(findAnagrams("ppqp","pq"))
print(findAnagrams("abbcabc","abc"))
print(findAnagrams("apapapa","apa"))


# Smallest Window containing Substring

def smallestWindowContainingSub(s1, subS):
    lettersFrequency = {}
    smallest = s1
    current = ""
    windowStart = 0
    matched = 0

    for char in subS:
        if char not in lettersFrequency:
            lettersFrequency[char] = 0
        lettersFrequency[char] += 1

    for windowEnd in range(len(s1)):
        rightSide = s1[windowEnd]

        if rightSide in lettersFrequency:
            lettersFrequency[rightSide] -= 1
            if lettersFrequency[rightSide] == 0:
                matched += 1
            

        while matched == len(lettersFrequency):
            current = s1[windowStart:windowEnd + 1]
            if len(current) < len(smallest):
                smallest = current
            leftSide = s1[windowStart]
            if leftSide in lettersFrequency:
                if lettersFrequency[leftSide] == 0:
                    matched -= 1
                lettersFrequency[leftSide] += 1
            windowStart += 1
                

    if len(current) == 0:
        return ""
    else:
        return smallest

print("smallest substring containing pattern")
print(smallestWindowContainingSub("aabdec", "abc"))
print(smallestWindowContainingSub("aabdec", "abac"))
print(smallestWindowContainingSub("abdbca", "abc"))
print(smallestWindowContainingSub("adcad", "abc"))    


# Words Concatenation

def wordConcatenation(str2,words):
    rightSide = ""
    windowStart = 0
    outputArr = []
    wordsHash = {}
    matched = 0
    #patternSize = len(words[0]) * len(words)
    wordSize = len(words[0])

    #create a dictionary from words
    for word in words:
        if word not in wordsHash:
            wordsHash[word] = 0
        wordsHash[word] += 1
    
    for windowEnd in range(len(str2)):
        rightSide += str2[windowEnd]
        if len(rightSide) == wordSize :
            if rightSide in wordsHash:
                wordsHash[rightSide] -= 1
            if wordsHash[rightSide] == 0:
                matched += 1
            if wordsHash[rightSide] < 0:
                windowStart = windowEnd - wordSize + 1
            rightSide = ""
        if len(wordsHash) == matched:
            wordsHash[str2[windowStart:windowStart + wordSize]] += 1
            matched -= 1 
            outputArr.append(windowStart)
            windowStart = windowEnd - wordSize + 1
        
    return outputArr
        
print("Words Concatenation")      
print(wordConcatenation("catfoxcat",["cat", "fox"]))
print(wordConcatenation("catcatfoxfox",["cat", "fox"]))


    
        

    



    

    

        







