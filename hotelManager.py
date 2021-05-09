# read no ofcustomers
noOfCustomers = int(input())

# read each customer happiness quotient
customersHappinessQuotient = []
for i in range(noOfCustomers):
    happinessQuotient = int(input())
    customersHappinessQuotient.append(happinessQuotient)

# prioritize which customers to serve first
proritizedCustomersWithHappinessQuotient = sorted(customersHappinessQuotient)

minUnhappiness = 0
time = 1

for customerHappinessQuotient in proritizedCustomersWithHappinessQuotient:
    minUnhappiness = minUnhappiness + abs(customerHappinessQuotient-time)
    time = time+1

print(minUnhappiness)
