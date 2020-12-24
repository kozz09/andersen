array = []
amount = int(input('Input amount of the numbers: '))
k = 1
for i in range(amount):
    number = int(input(f'Input number {k}: '))
    k+=1
    if (number % 3 == 0):
        array.append(number)
    
print('Numbers multiple of 3: ' + str(array))
k = input('\nPress Enter for exit')
