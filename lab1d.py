
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Colin Spagnuolo
# Date: September 18th, 2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py
name = "colin spagnuolo"
name = name.upper()
age = 23
Birthday_message = "How are you {name}? Happy {age}rd birthday!".format(name=name, age=age)
print(Birthday_message)
words = "The quick brown fox jumps over the lazy dog"
first_c = words[0]
seventeenth_c = words[16]
print("The first character is: ", first_c)
print("The seventeenth character is: ", seventeenth_c)
jumps = words[-20:-15]
quick = words[-43:-38]
print(jumps)
print(quick)
words_slice = words[2:15]
print(words_slice)
words_slice2 = words[5:22]
print(words_slice2)
