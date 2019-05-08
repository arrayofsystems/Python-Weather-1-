highAvg = 0
lowAvg = 0

#Enter the range of the area
zipmin = input("Enter the lowest zip code:")
zipmax = input("Enter the highest zip code:")


#Enter the highs and lows for each day. input() gives a string value. int(input()) gives an integer
monHigh = int(input("Please enter Monday's high tempurature for area " +  zipmin + " - " + zipmax + ":"))
monLow = int(input("Please enter Monday's low tempurature for area " +  zipmin + " - " +zipmax + ":"))
tueHigh = int(input("Please enter Tuesday's high tempurature for area " +  zipmin + " - "+ zipmax + ":"))
tueLow = int(input("Please enter Tuesday's low tempurature for area " +  zipmin + " - " +zipmax + ":"))
wedHigh = int(input("Please enter Wednesday's high tempurature for area " +  zipmin + " - "+ zipmax + ":"))
wedLow = int(input("Please enter Wednesday's low tempurature for area " +  zipmin + " - "+ zipmax + ":"))
thuHigh = int(input("Please enter Thursday's high tempurature for area " +  zipmin + " - " +zipmax + ":"))
thuLow = int(input("Please enter Thursday's low tempurature for area " +  zipmin + " - " +zipmax + ":"))
friHigh = int(input("Please enter Friday's high tempurature for area " +  zipmin + " - " +zipmax + ":"))
friLow = int(input("Please enter Friday's low tempurature for area " +  zipmin + " - " +zipmax + ":"))


#The average high and low. 
highAvg = float((monHigh +  tueHigh +  wedHigh +  thuHigh +  friHigh))  / 5
lowAvg =  float((monLow +  tueLow +   wedLow +   thuLow +  friLow))  / 5 

#Enter your zip code
zipCode = input("Please Enter your zipcode")

#This code only executes, if your zip code is in range
if zipCode >= zipmin and zipCode <= zipmax:
    print("Mondays high is " + str(monHigh))
    print("Mondays low is " + str(monLow))
    print("Mondays high is " + str(tueHigh))
    print("Mondays low is " + str(tueLow))
    print("Mondays high is " + str(wedHigh))
    print("Mondays low is " + str(wedLow))
    print("Mondays high is " + str(thuHigh))
    print("Mondays low is " + str(thuLow))
    print("Mondays high is " + str(friHigh))
    print("Mondays low is " + str(friLow))
    print("The high average tempurature is " + str(highAvg))
    print("The high average tempurature is " + str(lowAvg))

    
else:
    print("Out of range!")
