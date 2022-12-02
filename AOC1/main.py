

f = open("input.txt", 'r')
# Input is a list each line of the input file as string
input = f.readlines()

# Convert everly line to an int
#input = [eval(i) for i in input]

# Loop over input lines:
most_calories = 0
current_calories = 0

most_calories_2 = 0
most_calories_3 = 0

for line in input:
    if (line == "\n"):
        if current_calories > most_calories:
            most_calories_3 = most_calories_2
            most_calories_2 = most_calories
            most_calories =  current_calories
        elif current_calories  > most_calories_2:
            most_calories_3 = most_calories_2
            most_calories_2 = current_calories
        elif current_calories > most_calories_3:
            most_calories_3 = current_calories
                    
        current_calories = 0

    else:
        current_calories += eval(line)
        
print(most_calories)    
print(most_calories_2)
print(most_calories_3)
print(most_calories + most_calories_2 + most_calories_3)