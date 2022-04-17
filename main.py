from tableDisplay import displayTickets
from tableDisplay import displayAttractions
from random import randint
from math import floor

tickets = ['One adult', 'One child', 'One senior', 'Family', 'Group']
attractions = ['Lion feeding', 'Penguin feeding', 'Evening BBQ']
validTickets = ['one adult', 'adult', 'one child', 'child' 'one senior', 'senior', 'family', 'group']
validAttractions = ['lion feeding', 'penguin feeding', 'evening bbq']
ticketPrices = [[20, 30], [12, 18], [16, 24], [60, 90], [15, 22.5]]
attPrices = [2.5, 2, 5]

numOfDays = None
while not numOfDays:
    try:
        numOfDays = int(input('How many days do you want your tickets to be for?\n'))
    except ValueError:
        numOfDays = None
        print('Please enter an integer value.')
    if numOfDays != 1 and numOfDays != 2:
        numOfDays = None
        print('Your number of days must be either 1 or 2.')

ticketsWanted = []
attractionsWanted = []
totalCost = 0
Done = False
global numOfPeople
numOfPeople = None
global numOfPeopleInFamily
numOfPeopleInFamily = 0
global numOfAdultsInGroup
global numOfChildrenInGroup
global numOfSeniorsInGroup
numOfAdultsInGroup = None
numOfSeniorsInGroup = None
numOfChildrenInGroup = None
while not Done:

    ticket1 = None
    while not ticket1:
        ticket1 = input('Which ticket would you like?\n')
        ticket1 = ticket1.lower()
        if ticket1 not in validTickets:
            ticket1 = None
            print('That was not a valid ticket, please try again.')

    if ticket1 == 'adult':
        ticket1 = 'one adult'
    if ticket1 == 'child':
        ticket1 = 'one child'
    if ticket1 == 'senior':
        ticket1 = 'one senior'

    amount = None
    if ticket1 != 'family' and ticket1 != 'group':
        while not amount:
            try:
                amount = int(input('How many of these tickets would you like?\n'))
            except ValueError:
                amount = None
                print("Please enter an integer value, eg. '1'")
        ticket1 = tickets[validTickets.index(ticket1)]
        for i in range(amount):
            ticketsWanted.append(ticket1)

    elif ticket1 == 'family':
        numOfAdults = None
        numOfSeniors = None
        numOfChildren = None
        while numOfAdults == None:
            try:
                numOfAdults = int(input('How many adults will be part of this ticket? Note - This does not mean seniors\n'))
            except ValueError:
                numOfAdults = None
                print('Please enter an integer value.')
            if numOfAdults > 2 or numOfAdults < 0:
                numOfAdults = None
                print('You can have a minimum of 0 and a maximum of 2 adult members.')

        while numOfSeniors == None:
            try:
                numOfSeniors = int(input('How many seniors will be part of this ticket?\n'))
            except ValueError:
                numOfSeniors = None
                print('Please enter an integer value.')
            if numOfSeniors + numOfAdults > 2 or numOfSeniors + numOfAdults < 1:
                numOfSeniors = None
                print('Your adult + senior members must total to either 1 or 2. No more, no less.')
            elif numOfSeniors > 2 or numOfSeniors < 0:
                numOfSeniors = None
                print('You can have a minimum of 0 and a maximum of 2 senior members.')

        while not numOfChildren:
            try:
                numOfChildren = int(input('How many children will be part of this ticket?\n'))
            except ValueError:
                numOfChildren = None
                print('Please enter an integer value.')
            if numOfChildren > 3 or numOfChildren < 0:
                numOfChildren = None
                print('You can have a minimum of 0 and a maximum of 3 child members.')

        for i in range(numOfAdults):
            ticketsWanted.append('One adult')
        for i in range(numOfSeniors):
            ticketsWanted.append('One senior')
        for i in range(numOfChildren):
            ticketsWanted.append('One child')
        numOfPeopleInFamily += numOfAdults + numOfSeniors + numOfChildren

    elif ticket1 == 'group':
        groupDone = False
        while not groupDone:
            while numOfAdultsInGroup == None:
                try:
                    numOfAdultsInGroup = int(input('How many adults will be part of this ticket? Note - This does not mean seniors\n'))
                except ValueError:
                    numOfAdultsInGroup = None
                    print('Please enter a positive integer value.')
                if numOfAdultsInGroup < 0:
                    numOfAdultsInGroup = None
                    print('You cannot have less than 0 adults. Please enter a positive integer.')

            while numOfSeniorsInGroup == None:
                try:
                    numOfSeniorsInGroup = int(input('How many seniors will be part of this ticket?\n'))
                except ValueError:
                    numOfSeniorsInGroup = None
                    print('Please enter a positive integer value.')
                if numOfSeniorsInGroup < 0:
                    numOfSeniorsInGroup = None
                    print('You cannot have less than 0 seniors. Please enter a positive integer.')

            while not numOfChildrenInGroup:
                try:
                    numOfChildrenInGroup = int(input('How many children will be part of this ticket?\n'))
                except ValueError:
                    numOfChildrenInGroup = None
                    print('Please enter a positive integer value.')
                if numOfChildrenInGroup < 0:
                    numOfChildrenInGroup = None
                    print('You cannot have less than 0 children. Please enter a positive integer.')

            numOfPeople += numOfAdultsInGroup + numOfSeniorsInGroup + numOfChildrenInGroup
            if numOfPeople < 6:
                numOfAdultsInGroup = None
                numOfSeniorsInGroup = None
                numOfChildrenInGroup = None
                print('This group ticket is not valid, please try again.')
                groupDone = False
            else:
                for i in range(numOfAdultsInGroup):
                    ticketsWanted.append('One adult')
                for i in range(numOfSeniorsInGroup):
                    ticketsWanted.append('One senior')
                for i in range(numOfChildrenInGroup):
                    ticketsWanted.append('One child')
                    groupDone = True

    isDone = None
    while not isDone:
        isDone = input('Would you like to purchase any more tickets? (Y/N)\n')
        isDone = isDone.lower()
        if isDone == 'yes':
            isDone = 'y'
        if isDone == 'no':
            isDone = 'n'
        if isDone != 'y' and isDone != 'n':
            print("Please enter either 'Y' or 'N'.")
            isDone = None
    if isDone.lower() == 'n':
        Done = True

wantsAttractions = None
while not wantsAttractions and len(attractionsWanted) <= 3:
    wantsAttractions = input('Would you like to add attractions to your cart (Y/N)? Note - this applies to all tickets chosen\n')
    wantsAttractions = wantsAttractions.lower()
    if wantsAttractions == 'yes':
        wantsAttractions = 'y'
    if wantsAttractions == 'no':
        wantsAttractions = 'n'
    if wantsAttractions != 'y' and wantsAttractions != 'n':
        print("Please enter either 'Y' or 'N'.")
        wantsAttractions = None

if wantsAttractions == 'y':
    wantsAttractions = True
if wantsAttractions == 'n':
    wantsAttractions = False

attractionsDone = False
while not attractionsDone and wantsAttractions:
    att1 = None
    while not att1:
        att1 = input('Which attraction would you like?\n')
        att1 = att1.lower()
        if att1 not in validAttractions:
            att1 = None
            print('Try again')
        if numOfDays == '1' and att1 == 'evening bbq':
            print('You cannot purchase the evening BBQ for 1 day tickets.')
        if att1 in attractionsWanted:
            print('Cannot have 2 of the same attractions. Please try again.')

    att1 = attractions[validAttractions.index(att1)]
    attractionsWanted.append(att1)

    isDone = None
    while not isDone:
        isDone = input('Would you like to purchase any more attractions? (Y/N)\n')
        if isDone.lower() != 'y' and isDone.lower() != 'n':
            print("Please enter either 'Y' or 'N'.")
            isDone = None
        if isDone.lower() == 'n':
            attractionsDone = True

adultCount = 0
childCount = 0
seniorCount = 0
for ticket in ticketsWanted:
    if ticket == 'One adult':
        adultCount += 1
    if ticket == 'One child':
        childCount += 1
    if ticket == 'One senior':
        seniorCount += 1

validOrder = True
if childCount > 2*(adultCount+seniorCount):
    print('Too many children tickets for adult tickets. An adult may bring up to two children.')
    validOrder = False

for i in range(floor(adultCount/2)):
    while childCount >= 2:
        adultCount -= 2
        ticketsWanted.remove('One adult')
        ticketsWanted.remove('One adult')
        if childCount >= 3:
            ticketsWanted.remove('One child')
            ticketsWanted.remove('One child')
            ticketsWanted.remove('One child')
            childCount -= 3
        elif childCount == 2:
            ticketsWanted.remove('One child')
            ticketsWanted.remove('One child')
            childCount -= 2

        ticketsWanted.append('Family')

        if seniorCount >= 1 and adultCount == 1:
            adultCount -= 1
            ticketsWanted.remove('One adult')
            seniorCount -= 1
            ticketsWanted.remove('One senior')
            if childCount > 2:
                childCount -= 3
                ticketsWanted.remove('One child')
                ticketsWanted.remove('One child')
                ticketsWanted.remove('One child')
            else:
                childCount -= 2
                ticketsWanted.remove('One child')
                ticketsWanted.remove('One child')

            ticketsWanted.append('Family')

        break

while childCount >= 2:
    if seniorCount >= 1 and adultCount == 1:
        adultCount -= 1
        ticketsWanted.remove('One adult')
        seniorCount -= 1
        ticketsWanted.remove('One senior')
        if childCount > 2:
            childCount -= 3
            ticketsWanted.remove('One child')
            ticketsWanted.remove('One child')
            ticketsWanted.remove('One child')
        else:
            childCount -= 2
            ticketsWanted.remove('One child')
            ticketsWanted.remove('One child')

        ticketsWanted.append('Family')


for i in range(floor(seniorCount/2)):
    while childCount >= 3:
        seniorCount -= 2
        ticketsWanted.remove('One senior')
        ticketsWanted.remove('One senior')

        ticketsWanted.remove('One child')
        ticketsWanted.remove('One child')
        ticketsWanted.remove('One child')
        childCount -= 3

        ticketsWanted.append('Family')

# TODO need to account for attractions here using attractionsWanted
# TODO use the num of adults, children and seniors in the first loop to add attraction prices for family tickets
# TODO global num of adults, children and seniors in group to then add cost as group tickets but then remove them from the ticketsWanted list before second cost loop runs
    # numOfPeople = adults + children + seniors
# TODO add to the algorithm to take all remaining tickets and just turn them into group if possible? may be the best way to do this, or at least get close, but does not offer absolute best prices.

totalCost = 0
for ticket in ticketsWanted:
    totalCost += ticketPrices[tickets.index(ticket)][numOfDays - 1]
    if ticket != 'Family':
        for attraction in attractionsWanted:
            totalCost += attPrices[attractions.index(attraction)]
if numOfPeopleInFamily:
    for person in range(numOfPeopleInFamily):
        for attraction in attractionsWanted:
            totalCost += attPrices[attractions.index(attraction)]

if numOfPeople:
    ticketsWanted.append('Group')
    if numOfDays == 1:
        totalCost += 15*numOfPeople
    if numOfDays == 2:
        totalCost += 22.5*numOfPeople

if validOrder:
    bookingNum = randint(0, 9999)
    print('The tickets in your basket:')
    for ticket in ticketsWanted:
        print(ticket)
    if len(attractionsWanted) >= 1:
        print('\nThe attractions you have booked for these tickets:')
        for attraction in attractionsWanted:
            print(attraction)

    print(f'\n\nTotal cost: ${totalCost} and your booking number is: {bookingNum}')

else:
    print('This booking is invalid. Please retry your booking.')

# TODO add attraction prices accordingly (per person)