import sys

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

    pick_consonants = sum(types['vowels'].values()) + 2*(sum(types['consonants'].values()) - max(types['consonants'].values()))
    pick_vowels = sum(types['consonants'].values()) + 2*(sum(types['vowels'].values()) - max(types['vowels'].values()))

    return(min(pick_consonants, pick_vowels))



input = []
output = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        input.append(line.rstrip().upper())
f.close()

cases = int(input.pop(0))

for i in range(cases):
    output.append('Case #{}: {}'.format(i+1, frequency_generator(input[i])))

with open(sys.argv[2], 'w') as f:
    for line in output:
        print(line)
        f.write(line + "\n")
f.close()

