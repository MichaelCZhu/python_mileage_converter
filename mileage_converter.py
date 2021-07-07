print("Please input the number of kilometers you ran today. The program will convert it into miles.")
kilometers = float(input())
miles = kilometers * 0.621371
rounded_miles = round(miles, 2)
print("So you ran " + f"{kilometers}" + " kilometers today.")
print("That converts to about " + f"{rounded_miles}" + " miles!")
