tickets = ['One adult', 'One child', 'One senior', 'Family', 'Group']
attractions = ['Lion feeding', 'Penguin feeding', 'Evening BBQ']
ticketsStripped = ['oneadult', 'onechild', 'onesenior', 'forfamily', 'sixormore']
ticketPrices = [[20, 30], [12, 18], [16, 24], [60, 90], [15, 22]]
attractionsStripped = ['lion feeding', 'penguin feeding', 'night barbecue']
attractionPrices = [2.5, 2, 5]
items = []
totalCost = 0


def displayTickets():
    print('\n' + '-' * 78 + '\n|\t\tTicket Types\t\t|\tCost for one day\t|\tCost for two days\t|\n' + '-' * 78)
    for i in range(3):
        print('|\t\t' + tickets[i] + '\t\t\t|\t\t\t$' + str(ticketPrices[i][0]) + '\t\t\t|\t\t\t$' + str(ticketPrices[i][1]) + '\t\t\t|\n' + '-' * 78)
    for i in range(3, 5):
        print('|\t\t' + tickets[i] + '\t\t\t\t|\t\t\t$' + str(ticketPrices[i][0]) + '\t\t\t|\t\t\t$' + str(ticketPrices[i][1]) + '\t\t\t|\n' + '-' * 78)


def displayAttractions():
    print('\n' + '-' * 48)
    print('|\t\tAttraction\t\t\t|\t\tCost\t\t|')
    print('-' * 48)

    for i in range(2):
        if i == 0:
            print('|\t\t' + attractions[i] + '\t\t|\t\t$' + str(attractionPrices[i]) + '\t\t|')
            print('-' * 48)
        else:
            print('|\t\t' + attractions[i] + '\t\t|\t\t$' + str(attractionPrices[i]) + '\t\t\t|')
            print('-' * 48)
    print('|\t\t' + attractions[2] + '\t\t\t|\t\t$' + str(attractionPrices[2]) + '\t\t\t|')
    print('-' * 48)

displayTickets()
displayAttractions()