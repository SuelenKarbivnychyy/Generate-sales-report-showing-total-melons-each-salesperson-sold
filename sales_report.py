"""Generate sales report showing total melons each salesperson sold."""


salespeople = []  #creating a empty list to hold 
melons_sold = [] #creating a empty list to hold the melons sold information

f = open('sales-report.txt') #opening the file

for line in f: #iterating through each line from file 
    line = line.rstrip() # cutting out any white space from the end of each line
    entries = line.split('|') #spliting each line in the given separator
    salesperson = entries[0] #assingin the first index item of each line to a a variable
    melons = int(entries[2]) # assingin the aumont of melon (from index 2) to a variable

    if salesperson in salespeople: #checking if current person is in the list salespeople
        position = salespeople.index(salesperson) # get the position of ocurrence of that person in salespeople list
        melons_sold[position] += melons # adding the aumont of melons sold by that person to melons_sold list and summing with aumont already there
        
    else:
        salespeople.append(salesperson) #if person not in the list, append it and the aumont of melon to the list
        melons_sold.append(melons) 


for i in range(len(salespeople)): #iterating through the salespeople list by index
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #priting name of person and how much melon it sold