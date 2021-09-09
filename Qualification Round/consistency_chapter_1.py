"""
------------------------------------------------------
FB Hackecup 2021: A1 Consistency Chapter 1

(c) 2021 Julie Co, Manila, Philippines
Facebook Hacker Cup 2021 - Qualification Round
https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/A1
------------------------------------------------------
""" 

import sys

# Frequency tally for each unique letter in a string
# Returns minimum number of changes required to make a consistent string (same character)
def frequency_generator(input):
    vowels = ['A', 'E', 'I', 'O', 'U']
    types = {'consonants': {'': 0}, 'vowels': {'': 0}}
    input_length = len(input)
    for x in input:
        if x in vowels:
            if x in types['vowels']:
                types['vowels'][x] += 1
            else:
                types['vowels'][x] = 1
        else:
            if x in types['consonants']:
                types['consonants'][x] += 1
            else:
                types['consonants'][x] = 1
                
                
    #Sample value for types object if input is 'BANANA'
    #types = {'consonants':{'':0, 'B':1, 'N':2}, 'vowels':{'':0, 'A':3}}

    #Get least number of changes if we pick a consonant consistent string           
    pick_consonants = sum(types['vowels'].values()) + 2*(sum(types['consonants'].values()) - max(types['consonants'].values()))
    
    #Get least number of changes if we pick a vowel consistent string
    pick_vowels = sum(types['consonants'].values()) + 2*(sum(types['vowels'].values()) - max(types['vowels'].values()))

    return(min(pick_consonants, pick_vowels))



input = []
output = []

# Read input
with open(sys.argv[1], 'r') as f:
    for line in f:
        input.append(line.rstrip().upper())
f.close()



cases = int(input.pop(0))

for i in range(cases):
    output.append('Case #{}: {}'.format(i+1, frequency_generator(input[i])))

    

# Write output
with open(sys.argv[2], 'w') as f:
    for line in output:
        print(line)
        f.write(line + "\n")
f.close()

