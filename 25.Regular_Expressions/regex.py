"""
1. What is RegEx? - Defining a search pattern
- Most used in validations
- Search engines
- Operations on strings
- Email validation

www.pythex.org
www.regex101.com

2. Syntax
\d - Returns a match where the string contains digits(0-9) \d+
\D - DOES NOT contain digits
\b - Returns a match where the specified characters are at the beginning or end of a word
\s - Returns a match where the string contains a white space character
\S - Returns a match where the string DOES NOT contain a white space character
\w - Returns a match where the string contains a word (a single letter included)
\W - Returns a match where the string DOES NOT contain a word (whitespace, symbols)

3. Metacharacters

. (DOT)	Matches any character except a newline.
^ (Caret)	Matches pattern only at the start of the string.
$ (Dollar)	Matches pattern at the end of the string
* (asterisk)	Matches 0 or more repetitions of the regex.
+ (Plus)	Match 1 or more repetitions of the regex.
? (Question mark)	Match 0 or 1 repetition of the regex.
[] (Square brackets)	Used to indicate a set of characters. Matches any single character in brackets. For example, [abc] will match either a, or, b, or c character
| (Pipe)	used to specify multiple patterns. For example, P1|P2, where P1 and P2 are two different regexes.
\ (backslash)	Use to escape special characters or signals a special sequence. For example, If you are searching for one of the special characters you can use a \ to escape them
[^...]	Matches any single character not in brackets.
(...)	Matches whatever regular expression is inside the parentheses. For example, (abc) will match to substring 'abc'


match:
last word - \w+$
first word - ^\w+

4. Sets

[arn]	Returns a match where one of the specified characters (a, r, or n) are present
[a-n]	Returns a match for any lower case character, alphabetically between a and n
[^arn]	Returns a match for any character EXCEPT a, r, and n
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9]	Returns a match for any digit between 0 and 9
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

#  Valid year format  12-Aug-2000 type
\d{1,2}-[A-Z][a-z]{2}-\d{4}

#  Valid email
[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+ # . not as functionality, but as a symbol

#(F\w+) - Matching a word starting with a specific letter

# re.search("regex", "searched content")


5. Flags

re.A	re.ASCII	Perform ASCII-only matching instead of full Unicode matching
re.I	re.IGNORECASE	Perform case-insensitive matching
re.M	re.MULTILINE	This flag is used with metacharacter ^ (caret) and $ (dollar).
When this flag is specified, the metacharacter ^ matches the pattern at beginning of the string and each newline’s beginning (\n).
And the metacharacter $ matches pattern at the end of the string and the end of each new line (\n)
re.S	re.DOTALL	Make the DOT (.) special character match any character at all, including a newline. Without this flag, DOT(.) will match anything except a newline
re.X	re.VERBOSE	Allow comment in the regex. This flag is useful to make regex more readable by allowing comments in the regex.
re.L	re.LOCALE	Perform case-insensitive matching dependent on the current locale. Use only with bytes patterns



"""


