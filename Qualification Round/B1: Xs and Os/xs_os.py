import sys

input = []
output = []

with open(sys.argv[1], 'r') as f:
    for line in f:
        input.append(line.strip())

f.close()

cases = int(input.pop(0))
num = 0

while(len(input)>0):
    num += 1
    n = int(input.pop(0))
    count_wins = {}
    min_moves = n
    matrix = []
    for i in range(n):
        row = []
        newline  = input.pop(0)
        for x in newline:
            row.append(x)
        matrix.append(row)
    
    for trans in [*zip(*matrix)]:
        matrix.append(trans)

    for y in range(len(matrix)):
        move_sequence = []
        if 'O' not in matrix[y] and '.' in matrix[y]:
            for x in range(n):
                if(matrix[y][x] == '.'):
                    move_sequence.append((y%n*(y<n) + x*(y>=n), x*(y<n) +(y%n)*(y>=n)))
            
            if len(move_sequence) not in count_wins.keys():
                count_wins[len(move_sequence)] = [move_sequence]
            else:
                if move_sequence not in count_wins[len(move_sequence)]:
                    count_wins[len(move_sequence)].append(move_sequence)

    

    if len(count_wins) ==0:
        output.append('Case #{}: Impossible'.format(num))
    else:
        output.append("Case #{}: {} {}".format(num, min(count_wins), len(count_wins[min(count_wins)])))

with open(sys.argv[2], 'w') as f:
    for line in output:
        print(line)
        f.write(line + "\n")
f.close()
