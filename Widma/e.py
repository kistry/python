with open('test.out') as file:
    x = [
        line.split()[-2]
        for line in file
        if 'nuclear repulsion energy' in line
        ]
#energia = float(input(x))
#print(energia)
energia =x

energiaostatni=energia[-1]
print('nuclear repulsion energy=',energiaostatni)
print("ilość powtórzeń",+(len(energia)))

for i in range(len(energia)):
    print(energia[i])

x.clear()
