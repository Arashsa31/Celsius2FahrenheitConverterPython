# asks for the user input
print("Please enter the current temperature in Celsius: " , end="")

# takes the user input and places it into the cTemp variable 
cTemp = float(input())

# repeats what the user entered 	    
print("You entered the current temperature as",cTemp, "degrees in Celsius.")

# use the conversion formula to convert Celsius temperature to Fahrenheit temperature
fTemp = 9/5 * cTemp + 32

# prints the converted degree to the user
print("Your converted temperature of", cTemp, "Celsius in Fahrenheit is ", end="")

# rounds the final tempature
txt = "{:.3f}"
print(txt.format(fTemp))
