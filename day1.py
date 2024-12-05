with open('inputs/day1_input.txt', 'r') as file:
    content = file.read()

length = len(content)-1
floor = 0
i=0
while i <= length:
    if content[i] == "(":
        floor +=1
        i +=1
    elif content[i] == ")":
        floor -=1
        if floor ==-1:
            break
        i +=1
print (i+1)