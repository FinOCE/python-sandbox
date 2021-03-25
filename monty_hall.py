from random import randint

car = randint(1, 3)

valid = False
while valid == False:
    try:
        guess = int(input('What door? '))
        if guess > 3 or guess < 1:
            print('Invalid choice. Please try again.')
        else:
            valid = True
    except ValueError:
        print('Invalid choice. Please try again.')

no_car = [i for i in range(1, 4) if i != car and i != guess]
print(f'Its not in {no_car[randint(0, len(no_car))-1]}. Do you want to switch?')

q2 = input('Y/N ').upper()
while q2 != 'Y' and q2 != 'N':
    print('Invalid choice. Please try again.')
    q2 = input('Y/N ').upper()

other = [i for i in range(1, 4) if i != guess and i != no_car][0]
guess = other if q2 == 'Y' else guess

message = 'Congrats, you are right!' if guess == car else 'Sorry, you are wrong.'
print(message)