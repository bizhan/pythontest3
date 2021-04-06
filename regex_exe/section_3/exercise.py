import re
print("Hello Exercise")
#section 9:Raw Strings

#\n  new line
#\t tab character
#\U stands for unicode

#r changes the string to raw format
path = r"C:\Users\tasks\new"

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

#11: re.compile()
#need to create a pattern from string pattern
s = r"\d{4}" # string s pattern, 4 sequence digits
t = re.compile(s) # regex pattern made from string pattern

r = re.findall(t,string)
print(r) #['1998']


#13: re.search()
#re.search(pattern, string, flags)
#pattern: re pattern
#string: str
#flags: optional
r = re.search(r"\d{3}",string)
print(r) 
#match object, 
#span(15,18) slice from 15 to 18 is the match

#15 re.match
#\w match three cons. at beg of target
#\w does not match white spaces.
r = re.match(r"\w{3}", string)
print(r)

#17  re.fullmatch()
l = len(string)
result = re.fullmatch(r".{285}", string)

#19 findall methods
#matches are return as list of strings.
r = re.findall(r"\d{3}",string)
print(r) #['600','199','600']

#21 re.split()
#split method by certain delimiter
print(string.split(" "))
#\s match any white space \n, \t, \characters
r = re.split(r"\s",string)
print(r)
#\s{3} 3 consecative white spaces.

#23 re.sub()
# replacing one or more occurance from on str to another str
#re.sub(pattern, repl, string, count, flags)
# pattern: to look for
# repl: replacement
# count: max number of pattern default 0 all of them
#flags: options
r = re.sub(r"[A-Z]{2,}", "INDEX", string)
#character class [A-Z] all upper case
#how many times should preceding ch repeat {2,}
#preceding character repeat 2 times
print(r)
r = re.sub(r"[A-Z]{2,}", "INDEX", string, 2)
print(r) #only two times


