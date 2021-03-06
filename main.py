# Importing the tables to be displayed from external file
from tableDisplay import displayTickets
from tableDisplay import displayAttractions

from familyTicket import purchaseFamilyTicket
from groupTicket import purchaseGroupTicket

# Importing mathematical functions
from math import floor
from random import choice
from string import digits
from string import ascii_letters

# Declaring all variables storing the different tickets, attractions and their prices.
tickets = ['One adult', 'One child', 'One senior', 'Family', 'Group']
attractions = ['Lion feeding', 'Penguin feeding', 'Evening BBQ']
# Lowercase names of tickets and attractions for validation
validTicketsAll = ['one adult', 'adult', 'one child', 'child', 'one senior', 'senior', 'family', 'group']
validTicketsDisplay = ['one adult', 'one child', 'one senior', 'family', 'group']  # If the user types; 'adult', 'child' or 'senior', converted to these.
validAttractions = ['lion feeding', 'penguin feeding', 'evening bbq']
# Prices for tickets stored in a matrix, 1 day then 2 days. List within lists.
ticketPrices = [[20, 30], [12, 18], [16, 24], [60, 90], [15, 22.5]]
attPrices = [2.5, 2, 5]

# Variables necessary for purchasing. Keeps track of tickets in the shopping cart and the attractions they want.
ticketsWanted = []
attractionsWanted = []
totalCost = 0


# Asking user for the number of days they want their ticket to be for.
numOfDays = None
while not numOfDays:
    # Try and except to turn input into number value
    try:
        numOfDays = int(input('How many days do you want your tickets to be for? (1 or 2).\n'))
    except ValueError:
        numOfDays = None
        print('Please enter an integer value.')
    # If not either 1 or 2, restart and ask again
    if numOfDays != 1 and numOfDays != 2:
        numOfDays = None
        print('Your number of days must be either 1 or 2.')

# Variable to track if the ticketBooking is complete, will loop until it is.
ticketBookingDone = False
while not ticketBookingDone:
    displayTickets()  # Displaying table, imported from external file

    # Asking user which ticket they would like
    ticket1 = None
    while not ticket1:
        ticket1 = input('Which ticket would you like?\n')
        ticket1 = ticket1.lower() # Turning into lowercase for validation
        if ticket1 not in validTicketsAll: # If not valid, try again
            ticket1 = None
            print('That was not a valid ticket, please try again.')

    # Turning into native ticket names, in case user typed the shorthand of 'adult', 'child' or 'senior'
    if ticket1 == 'adult':
        ticket1 = 'one adult'
    if ticket1 == 'child':
        ticket1 = 'one child'
    if ticket1 == 'senior':
        ticket1 = 'one senior'

    # Asking user how many of a particular ticket they want, only done if it is an individual ticket
    amount = None
    if ticket1 != 'family' and ticket1 != 'group':
        # Loop to allow user to enter amount
        while not amount:
            # Try and except to turn input into number value
            try:
                amount = int(input('How many of these tickets would you like?\n'))
            except ValueError:
                amount = None
                print("Please enter an integer value, eg. '1'")

        # Turning ticket into display name, ie. 'one adult' --> 'One adult'
        ticket1 = tickets[validTicketsDisplay.index(ticket1)] # Using indexing to turn value into corresponding value from different list
        # Add the amount of tickets user wanted into shopping cart
        for i in range(amount):
            ticketsWanted.append(ticket1)

    # If user wants family ticket
    elif ticket1 == 'family':
        purchaseFamilyTicket()

    # If user wants group ticket
    elif ticket1 == 'group':
        purchaseGroupTicket()

    # Asking user if they want more tickets, decides whether or not loop continues or breaks
    isDone = None
    while not isDone:
        isDone = input('Would you like to purchase any more tickets? (Y/N)\n')
        isDone = isDone.lower() # Lowering all letters for validation

        # Accounting for full inputs of 'yes' or 'no'
        if isDone == 'yes':
            isDone = 'y'
        if isDone == 'no':
            isDone = 'n'

        # If not any desirable input, try again
        if isDone != 'y' and isDone != 'n':
            print("Please enter either 'Y' or 'N'.")
            isDone = None

    # If user says no more tickets, loop breaks. If user says yes, nothing happens and loop automatically continues
    if isDone.lower() == 'n':
        ticketBookingDone = True


# Asking user if they want to add attractions to their booking
wantsAttractions = None
while wantsAttractions is None:
    wantsAttractions = input('Would you like to add attractions to your cart (Y/N)? Note - this applies to all tickets chosen\n')
    wantsAttractions = wantsAttractions.lower() # Lowering all letters for validation

    # Accounting for full inputs of 'yes' or 'no'
    if wantsAttractions == 'yes':
        wantsAttractions = 'y'
    if wantsAttractions == 'no':
        wantsAttractions = 'n'

    # If not any desirable input, try again
    if wantsAttractions != 'y' and wantsAttractions != 'n':
        print("Please enter either 'Y' or 'N'.")
        wantsAttractions = None

    # If user said yes, setting wantsAttractions to true so the user can input which attractions they would like
    if wantsAttractions == 'y':
        wantsAttractions = True
    # If user said no, wantsAttractions is set to false and the booking will near completion
    if wantsAttractions == 'n':
        wantsAttractions = False


attractionsDone = False # Variable for whether or not loop should repeat, (repeats if user wants several attractions)
while not attractionsDone and wantsAttractions is True: # Only runs if user previously said they want attractions
    displayAttractions() # Displays table for attractions from external file

    # Asking user which attraction they would like
    att1 = None
    while not att1:
        att1 = input("Which attraction would you like? Type 'None' for no attraction.\n")
        att1 = att1.lower()
        if att1 not in validAttractions and att1 != 'none':
            att1 = None
            print('Try again')
        elif att1 in validAttractions:
            att1 = attractions[validAttractions.index(att1)]
        if numOfDays == 1 and att1 == 'Evening BBQ':
            att1 = None
            print('You cannot purchase the evening BBQ for 1 day tickets.')
        if att1 in attractionsWanted:
            att1 = None
            print('Cannot have 2 of the same attractions. Please try again.')
        if att1 == 'None':
            att1 = None
            break

    if att1 is not None and att1 != 'none':
        attractionsWanted.append(att1)

    isDone = None
    while not isDone:
        isDone = input('Would you like to purchase any more attractions? (Y/N)\n')
        isDone = isDone.lower()
        if isDone == 'yes':
            isDone = 'y'
        if isDone == 'no':
            isDone = 'n'
        if isDone != 'y' and isDone != 'n':
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
if childCount > 2 * (adultCount + seniorCount):
    print('Too many children tickets for adult tickets. An adult may bring up to two children.')
    validOrder = False

for ticket in ticketsWanted:
    for attraction in attractionsWanted:
        totalCost += attPrices[attractions.index(attraction)]

for i in range(floor(adultCount / 2)):
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

for i in range(floor(seniorCount / 2)):
    while childCount >= 3:
        seniorCount -= 2
        ticketsWanted.remove('One senior')
        ticketsWanted.remove('One senior')

        ticketsWanted.remove('One child')
        ticketsWanted.remove('One child')
        ticketsWanted.remove('One child')
        childCount -= 3

        ticketsWanted.append('Family')

num = 0
for ticket in ticketsWanted:
    if ticket != 'Family':
        num += 1

if num >= 6:
    for i in range(num):
        ticketsWanted.remove(ticketsWanted[0])

    ticketsWanted.append('Group')
    sizeOfGroup = num

for ticket in ticketsWanted:
    if ticket != 'Group':
        totalCost += ticketPrices[tickets.index(ticket)][numOfDays - 1]
    elif ticket == 'Group':
        if numOfDays == 1:
            totalCost += 15 * num
        elif numOfDays == 2:
            totalCost += 22.5 * num

if validOrder:
    bookingNum = ''.join([choice(ascii_letters + digits) for n in range(6)])
    print('The tickets in your basket:')
    for ticket in ticketsWanted:
        if ticket == 'Group':
            print(ticket, f'({num} people).')
        else:
            print(ticket)
    if len(attractionsWanted) >= 1:
        print('\nThe attractions you have booked for these tickets:')
        for attraction in attractionsWanted:
            print(attraction)

    print(f'\n\nTotal cost: ${totalCost} and your booking number is: {bookingNum}')

else:
    print('This booking is invalid. Please retry your booking.')
