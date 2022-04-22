# Essentials
tickets = ['One adult', 'One child', 'One senior', 'For Family', 'Six or more']
attractions = ['Lion feeding', 'Penguin feeding', 'Night Barbecue (2 day tickets only)']
oneDayPrices = [20, 12, 16, 60, 15]
twoDayPrices = [30, 18, 24, 90, 22]
attractionPrices = [2.5, 2, 5]


print('\nTicket Types\t\t|\t\tCost for one day')
for i in range(len(tickets)):
    print(tickets[i] + '\t\t\t|\t\t\t$' + str(oneDayPrices[i]))

print('\nTicket Types\t\t|\t\tCost for two days')
for i in range(len(tickets)):
    print(tickets[i] + '\t\t\t|\t\t\t$' + str(twoDayPrices[i]))



print('\nAttraction\t\t|\t\tCost')
for i in range(len(attractions)):
    print(attractions[i] + '\t\t|\t\t$' + str(attractionPrices[i]))




