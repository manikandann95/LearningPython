"Interacting with OS"

re module in python

```Python
import re
result = re.search(r'aza','plaza') # r indicates its a RawString
#Always use RawStrings for regex in python
print(result) # O/P: <re.Match object; span=(2,5), match='aza'> - our aza matches in span 2,5 in the given string
result = re.search(r'aza','bazaar') # r indicates its a RawString
print(result) # O/P: <re.match; span=(1,4), match='aza'> - our aza matches in span 1,4 in the given string i.e. result[1:4]
result = re.search(r'aza','maze') # O/P : None (since that substring is not match in given string)
print(result)
result = re.search(r'x','xerox')
print(result) # O/P : <re.match; span=(0,1), match='x'>
#-----------------------------------------------------
#Let's use special characters

result = re.search(r'p.ng','clapping')
print(result) #O/P: <re.Match object; span=(4, 8), match='ping'>

import re
def check_aei (text):
  result = re.search(r"a.e.i", text, re.IGNORECASE) # RE.IGNORECASE make sure case is not matter
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False (because exactly one gap in between each vowel need to be true in the same order aei)
print(check_aei("paraMEDIC")) # True
```
Character Classes : Inside Square brackets insert both letters to check if thats a match

```Python
import re

print(re.search(r'[Pp]ython', 'Python')) # O/P: <re.Match object; span=(0, 6), match='Python'>

print(re.search(r'[a-z]way', 'The end of the Highway')) # O/P: <re.Match object; span=(18,22), match='hway'>
# Ranges we can use are : A-Z a-z 0-9
print(re.search(r'cloud[a-zA-Z0-9]','cloudy weather')) # O/P: <re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r'cloud[a-zA-Z0-9]','cloud9 cinemas')) # O/P: <re.Match object; span=(0, 6), match='cloud9'>

print(re.search(r'[a-z]way', 'What a way to go')) # O/P: None (bcz the range of characters expected does not match)
```
```Python
# Check whether punctuation is present or not
import re
def check_punctuation (text):
  result = re.search(r"[.?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
```
If we need to match string with "Not having characters" we use NOT - caret (^)
If we need to match string with either string we use OR - vertical bar (|)

```Python
# Check whether the sentence has other than Alphabets
print(re.search(r'[^a-zA-Z]','This is a sentence with spaces.')) # O/P: <re.Match object; span=(4, 5), match=' '> # i.e O/P is First Space in the given sentence
print(re.search(r'[^a-zA-Z ]','This is a sentence with spaces.')) # O/P: <re.Match object; span=(30, 31), match='.'> # i.e O/P is first dot in the given sentence bcz space is given inside square bracket

print(re.search(r'[dog|cat]','I like dogs.')) # O/P: <re.Match object; span=(7, 10), match='dog'>
print(re.search(r'[dog|cat]','I like both cats and dogs.')) # O/P: <re.Match object; span=(12, 15), match='cat'>
```
