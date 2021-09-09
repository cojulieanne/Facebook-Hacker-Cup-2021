"""
------------------------------------------------------
FB Hackecup 2021: Xs and Os
(c) 2021 Julie Co, Manila, Philippines
Facebook Hacker Cup 2021 - Qualification Round
https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/B
------------------------------------------------------
"""


import sys

input = []
output = []

# Read Input
with open(sys.argv[1], 'r') as f:
    for line in f:
        input.append(line.strip())

f.close()


cases = int(input.pop(0))
num = 0

#Read lines based on number of rows declared by parameters per case
while(len(input)>0):
    
    num += 1
    n = int(input.pop(0))
    count_wins = {}
    min_moves = n
    matrix = []
    
    # Plot the XO board in a matrix
    for i in range(n):
        row = []
        newline  = input.pop(0)
        for x in newline:
            row.append(x)
        matrix.append(row)
    
    # Append the tranpose of the XO board in the same matrix to represent columns in row-wise fashion
    for trans in [*zip(*matrix)]:
        matrix.append(trans)

        
    for y in range(len(matrix)):
        
        move_sequence = []
        
        if 'O' not in matrix[y] and '.' in matrix[y]:       # Player can only choose rows that have no 'O' in a row or column
            
            for x in range(n):
                
                # Append the coordinates of the cells where a valid move can be made
                if(matrix[y][x] == '.'):
                    move_sequence.append((y%n*(y<n) + x*(y>=n), x*(y<n) +(y%n)*(y>=n)))
            
            # Keys of the dictionary will be based on number of moves/cells to win
            # Values of the dictionary will be a list of move sequences
            if len(move_sequence) not in count_wins.keys():
                count_wins[len(move_sequence)] = [move_sequence]
                
            else:
                
                # Append only if sequence does not exist yet to avoid duplication
                if move_sequence not in count_wins[len(move_sequence)]:
                    count_wins[len(move_sequence)].append(move_sequence)
    
    # No possible moves to win
    if len(count_wins) ==0:
        output.append('Case #{}: Impossible'.format(num))
        
    #Output minimum number of moves and number of ways this optimal win can be achieved
    else:
        output.append("Case #{}: {} {}".format(num, min(count_wins), len(count_wins[min(count_wins)])))

        
# Write output
with open(sys.argv[2], 'w') as f:
    for line in output:
        print(line)
        f.write(line + "\n")
f.close()
