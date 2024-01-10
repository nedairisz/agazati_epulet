def jatek():
    print('I/A:')
    nev = input('\tJátékos neve: ')
    szerep = input('\tszerepkör: ')
    print("I/B:")
    if szerep == 'varázsló':
        elet = 2
    elif szerep == 'harcos':
        elet = 10
    else:
        elet = 8
    print(f"\tÜdvözlünk {nev}, {elet} életed van!")