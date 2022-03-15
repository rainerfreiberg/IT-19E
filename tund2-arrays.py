from re import X


numbrid = []

mitu_vanust = int(input("Mitu vanust soovid sisestada?: "))


for i in range(0, mitu_vanust):
    number = int(input("Number " + str(i) + ": "))
    numbrid.append(number) 

summa = 0
for x in numbrid:
    summa = summa + x
print(summa / mitu_vanust)



#numbrid = []

#for i in range(0, 10)
#    number = int(input("Number " + str(i) + ": "))
#    numbrid.append(number) 

#for x in numbrid:
#    print(x)





#numbrid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#k6ige_suurem_number = 0
#for x in numbrid:
#    if x > k6ige_suurem_number:
#        k6ige_suurem_number = x
#print(k6ige_suurem_number)