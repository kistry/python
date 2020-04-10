with open('ir.txt') as file:
    y = [
        line.split()[-2]
        for line in file
        if '#' in line
             
        ]
        
print(y[1:])
 
#for i in range(len(y)):
#    print(y[3])
