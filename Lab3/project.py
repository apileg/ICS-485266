import random

deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
count = 0

random.shuffle(deck);

print('Поиграем в очко?')

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = deck.pop()
        print('Вам попалась карта достоинством %d' % current)
        count += current
        if count > 21:
            print('Извините, но вы проиграли')
            break
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            break
        else:
            print('У вас %d очков.' % count)
    elif choice == 'n':
        print('У вас %d очков и вы закончили игру.' % count)
        break

print('До новых встреч!')
