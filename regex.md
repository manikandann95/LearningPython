"Interacting with OS"

re module in python

^                Start of line/string.
[a-zA-Z]         Character is in a-z or A-Z.
[a-zA-Z0-9.,$;]  Alphanumeric or `.` or `,` or `$` or `;`.
+                One or more of the previous token (change to * for zero or more).
$                End of line/string.

(?:...)

    A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.


```Python
import re
result = re.search(r'aza','plaza') # r indicates its a RawString
#Always use RawStrings for regex in Python
print(result) # O/P: <re.Match object; span=(2,5), match='aza'> - our aza matches in span 2,5 in the given string
result = re.search(r'aza','bazaar') # r indicates its a RawString
print(result) # O/P: <re.match; span=(1,4), match='aza'> - our aza matches in span 1,4 in the given string i.e. result[1:4]
result = re.search(r'aza','maze') # O/P: None (since that substring does not match in the given string)
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
print(check_aei("aerial")) # False (because exactly one gap in between each vowel needs to be true in the same order aei)
print(check_aei("paraMEDIC")) # True
```
Character Classes: Inside Square brackets insert both letters to check if they match

```Python
import re

print(re.search(r'[Pp]ython', 'Python')) # O/P: <re.Match object; span=(0, 6), match='Python'>

print(re.search(r'[a-z]way', 'The end of the Highway')) # O/P: <re.Match object; span=(18,22), match='hway'>
# Ranges we can use are: A-Z a-z 0-9
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
print(re.search(r'[^a-zA-Z ]','This is a sentence with spaces.')) # O/P: <re.Match object; span=(30, 31), match='.'> # i.e O/P is the first dot in the given sentence bcz space is given inside the square bracket

print(re.search(r'[dog|cat]','I like dogs.')) # O/P: <re.Match object; span=(7, 10), match='dog'>
print(re.search(r'[dog|cat]','I like both cats and dogs.')) # O/P: <re.Match object; span=(12, 15), match='cat'>
print(re.findall(r'[dog|cat]','I like both cats and dogs')) # O/P: ['dog', 'cat'] # findall finds all the given substring

```
re.findall - finds all the given substrings
#------------------------------------------------------------------------------------------
How to match a certain character / Substring or string/sentence **Several Times**
Eg: We Need to find the longest word in the string / Find the hostnames in the log, 

for that we use **Repeated Matches**  : ".*" dot followed by star rather than single dot

This means It matches any character **repeated as many times as possible including Zero**

```Python
import re
print(re.search(r'Py.*n','Pygmalion')) # O/P: <re.Match object; span=(0,9), match='Pygmalion'>
print(re.search(r'Py.*n','Python Programming')) # O/P: <re.Match object; span=(0,17), match='Python Programmin'> # It takes the last 'n' in the given string, bcz Star takes as many characters as possible

#This **Star** qualifier behaviour is called **GREEDY**
# Program to check at least 2 a is present either lower or upper case
import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*[Aa]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

print(re.search(r'Py[a-z]*n','Python Programming')) # O/P: <re.Match object; span=(0, 6), match='Python'> bcz it won't take other than small alphabets in between
print(re.search(r'Py[a-z]*n','Pyn')) # O/P: <re.Match object; span=(0, 3), match='Pyn'> # Remember Unlike dot, star qualifier can have Zero characters too. 
```
Other than dot (.), and star (*), it can take Plus (+) and question mark (?) that help to create complex expressions like the "egrep" command
+ is for multiple times match,? Zero match also taken into count
\ is for escape character (\. \* \+ \? \$ \^ inside search) Eg: re.search(r'\.com','mydomain.com')
\w is wild search for one word {i.e. until space} ; \s for white space ; \d for digit

```Python
import re
# +
print(re.search(r'o+l+','goldfish') # <re.Match object; span=(1,3), match='ol'>
print(re.search(r'o+l+','woolly') # <re.Match object; span=(1,5), match='ooll'> # Same query gives as many o l presents concurrently
print(re.search(r'o+l+','boiling')) # None (bvcz its not concurrent)
# ?
print(re.search(r'p?each','each of us on our own')) # <re.Match object; span=(0,3), match='each'>
print(re.search(r'p?each','I like peaches')) # <re.Match object; span=(7,12), match='peach'>
# /w /d /s
print(re.search(r'\w*','Just a Sentence')) # <re.Match object; span=(0, 4), match='Just'>

print(re.search(r'\w*','123456789')) # <re.Match object; span=(0, 9), match='123456789'> This is also a word ahh

print(re.search(r'\d','Just 1 Sentence')) # <re.Match object; span=(5, 6), match='1'>
print(re.search(r'\d*','Just 1 Sentence')) # <re.Match object; span=(0, 0), match=''> ; d star, s star gives interesting o/p
print(re.search(r'\s','Just a Sentence')) # <re.Match object; span=(4, 5), match=' '>

print(re.search(r'\d*','Just a Sentence')) # <re.Match object; span=(0, 0), match=''>
```

```Python
# check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

import re
def check_character_groups(text):
    result = re.search(r"\w\s", text)
    return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
```
match() versus search()
The match() function only checks if the RE matches at the beginning of the string while search() will scan forward through the string for a match. It’s important to keep this distinction in mind. Remember, match() will only report a successful match which will start at 0; if the match wouldn’t start at zero, match() will not report it.

```Python
print(re.match('super', 'superstition').span()) # (0, 5)
print(re.match('super', 'insuperable')) # None

print(re.search('super', 'superstition').span()) # (0, 5)
print(re.search('super', 'insuperable').span()) # (2, 7)

s = '<html><head><title>Title</title>'
len(s) # 32
print(re.match('<.*>', s).span()) # (0, 32)
print(re.match('<.*>', s).group()) # <html><head><title>Title</title>


#  for example, a pattern starting with "Crow" must match starting with a 'C'. The analysis lets the engine quickly scan through the string looking for the starting character, only trying the full match if a 'C' is found.
# Adding .* defeats this optimization, requiring scanning to the end of the string and then backtracking to find a match for the rest of the RE. Use re.search() instead.
```

```Python
import re
def transform_record(record):
  new_record = re.sub(r',([\d\-]+),',r',+1-\1,', record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
```
```Python
import re
def multi_vowel_words(text):
  pattern = r'\w*(?:a|e|i|o|u){3,}\w*' (?:....) makes us to return a substring
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []
```
```Python
import re
def transform_comments(line_of_code):
  result = re.sub(r'(#+)','//', line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"
```
```Python
import re
def convert_phone_number(phone):
  result = re.sub(r'(\b\d{3})-(\d{3}-\d{4}\b)', r'(\1) \2', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
```

