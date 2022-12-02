f = open("input.txt", 'r')
# Input is a list each line of the input file as string
input = f.readlines()

# Convert everly line to an int
#input = [eval(i) for i in input]

#x = rock, y= paper, z = scissor
#A = rock, B = paper, C = scissor

choice_points = {'X' : 1, 'Y' : 2, 'Z' : 3}
choice_win = {('A', 'X') : 3, ('A', 'Y') : 6, ('A', 'Z') : 0,
              ('B', 'X') : 0, ('B', 'Y') : 3, ('B', 'Z') : 6,
              ('C', 'X') : 6, ('C', 'Y') : 0, ('C', 'Z') : 3}

choice_part2 = {('A', 'X') : 3, ('A', 'Y') : 4, ('A', 'Z') : 8,
              ('B', 'X') : 1, ('B', 'Y') : 5, ('B', 'Z') : 9,
              ('C', 'X') : 2, ('C', 'Y') : 6, ('C', 'Z') : 7}

sum = 0
# Loop over input lines:
for line in input:
    parts = line.split(' ')
    sum += choice_points[(parts[1][0])]
    sum += choice_win[(parts[0], parts[1][0])]
    
sum2 = 0
for line in input:
    parts = line.split(' ')
    sum2 += choice_part2[(parts[0], parts[1][0])]

print(sum2
      )