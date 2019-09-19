startNumber = int(input("Geef een begin getal:"))
endNumber = int(input("Geef een eind getal:"))

eString = ""
count = 0

for i in range(1, endNumber+1):
    eString = eString + str(startNumber) + "x" + str(i) + "=" + str(startNumber * i) + ","
    count = count + 1
    if(count == 3):
        print(eString[:-1])
        count = 0
        eString=""